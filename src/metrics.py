"""
Turns raw RPC / API payloads into the clean, judge-readable metrics
the bounty asks for. Every function is defensive: missing or malformed
upstream data yields `None` for that metric rather than raising, so a
partial outage never takes down the whole report.
"""
import statistics


def network_performance(onchain: dict) -> dict:
    samples = onchain.get("performance_samples") or []
    epoch_info = onchain.get("epoch_info") or {}

    tps_values, slot_time_values = [], []
    for s in samples:
        secs = s.get("samplePeriodSecs") or 0
        num_tx = s.get("numTransactions") or 0
        num_slots = s.get("numSlots") or 0
        if secs:
            tps_values.append(num_tx / secs)
        if num_slots:
            slot_time_values.append((secs / num_slots) * 1000)  # ms

    epoch_progress_pct = None
    if epoch_info.get("slotsInEpoch"):
        epoch_progress_pct = round(100 * epoch_info["slotIndex"] / epoch_info["slotsInEpoch"], 2)

    return {
        "current_slot": onchain.get("slot"),
        "current_epoch": epoch_info.get("epoch"),
        "epoch_progress_pct": epoch_progress_pct,
        "slot_index_in_epoch": epoch_info.get("slotIndex"),
        "slots_in_epoch": epoch_info.get("slotsInEpoch"),
        "avg_tps_recent": round(statistics.mean(tps_values), 2) if tps_values else None,
        "max_tps_recent": round(max(tps_values), 2) if tps_values else None,
        "avg_slot_time_ms": round(statistics.mean(slot_time_values), 2) if slot_time_values else None,
        "latest_block_time_unix": onchain.get("latest_block_time"),
        "cluster_health": onchain.get("health"),
    }


def validator_status(onchain: dict) -> dict:
    vote_accounts = onchain.get("vote_accounts") or {}
    current = vote_accounts.get("current") or []
    delinquent = vote_accounts.get("delinquent") or []

    total_validators = len(current) + len(delinquent)
    delinquency_pct = round(100 * len(delinquent) / total_validators, 2) if total_validators else None

    total_stake = sum(v.get("activatedStake", 0) for v in current + delinquent)
    ranked = sorted(current, key=lambda v: v.get("activatedStake", 0), reverse=True)
    top_validators = [
        {
            "vote_pubkey": v.get("votePubkey"),
            "node_pubkey": v.get("nodePubkey"),
            "activated_stake_sol": round(v.get("activatedStake", 0) / 1_000_000_000, 2),
            "stake_share_pct": round(100 * v.get("activatedStake", 0) / total_stake, 3) if total_stake else None,
            "commission_pct": v.get("commission"),
        }
        for v in ranked[:10]
    ]

    commissions = [v.get("commission") for v in current if v.get("commission") is not None]

    return {
        "active_validator_count": len(current),
        "delinquent_validator_count": len(delinquent),
        "delinquency_pct": delinquency_pct,
        "total_active_stake_sol": round(total_stake / 1_000_000_000, 2) if total_stake else None,
        "top_validators_by_stake": top_validators,
        "avg_commission_pct": round(statistics.mean(commissions), 2) if commissions else None,
        "median_commission_pct": round(statistics.median(commissions), 2) if commissions else None,
        "zero_commission_validator_count": sum(1 for c in commissions if c == 0),
    }


def fee_and_rev_estimate(onchain: dict, sol_price_usd) -> dict:
    block = onchain.get("sample_block")
    if not block:
        return {
            "sample_available": False,
            "median_fee_lamports": None,
            "mean_fee_lamports": None,
            "sampled_transaction_count": 0,
            "estimated_rev_sol_per_block": None,
            "estimated_rev_usd_per_block": None,
            "note": "No finalized block sample available this run (RPC miss/timeout).",
        }

    fees = []
    for tx in block.get("transactions", []):
        meta = tx.get("meta") or {}
        fee = meta.get("fee")
        if fee is not None:
            fees.append(fee)

    if not fees:
        return {
            "sample_available": False,
            "median_fee_lamports": None,
            "mean_fee_lamports": None,
            "sampled_transaction_count": 0,
            "estimated_rev_sol_per_block": None,
            "estimated_rev_usd_per_block": None,
            "note": "Sampled block had no transactions with fee metadata.",
        }

    total_fees_lamports = sum(fees)
    total_fees_sol = total_fees_lamports / 1_000_000_000
    result = {
        "sample_available": True,
        "sampled_slot": block.get("parentSlot", None),
        "sampled_transaction_count": len(fees),
        "median_fee_lamports": statistics.median(fees),
        "mean_fee_lamports": round(statistics.mean(fees), 2),
        # REV here = base + priority fees actually paid in the sampled block.
        # This intentionally excludes MEV/tips routed off-chain, which no
        # keyless public source can see — see README "REV methodology".
        "estimated_rev_sol_per_block": round(total_fees_sol, 6),
        "estimated_rev_usd_per_block": round(total_fees_sol * sol_price_usd, 4) if sol_price_usd else None,
        "note": "REV estimate = base+priority fees from one sampled finalized block. Excludes off-chain MEV.",
    }
    return result


def economic_indicators(offchain: dict, fee_estimate: dict) -> dict:
    price_data = (offchain.get("sol_price") or {}).get("solana", {})
    tvl_history = offchain.get("tvl_history") or []
    dex_overview = offchain.get("dex_overview") or {}
    stablecoins = offchain.get("stablecoin_supply") or []

    current_tvl = tvl_history[-1]["tvl"] if tvl_history else None
    tvl_24h_ago = tvl_history[-2]["tvl"] if len(tvl_history) >= 2 else None
    tvl_change_pct = None
    if current_tvl is not None and tvl_24h_ago:
        tvl_change_pct = round(100 * (current_tvl - tvl_24h_ago) / tvl_24h_ago, 2)

    current_stablecoin_supply = None
    if stablecoins:
        latest_point = stablecoins[-1]
        # DeFiLlama returns totalCirculating as a dict keyed by peg type (e.g. peggedUSD)
        circulating = latest_point.get("totalCirculating", {})
        current_stablecoin_supply = sum(circulating.values()) if isinstance(circulating, dict) else circulating

    return {
        "sol_price_usd": price_data.get("usd"),
        "sol_price_change_24h_pct": round(price_data.get("usd_24h_change", 0), 2) if price_data.get("usd_24h_change") is not None else None,
        "sol_market_cap_usd": price_data.get("usd_market_cap"),
        "sol_24h_volume_usd": price_data.get("usd_24h_vol"),
        "solana_tvl_usd": current_tvl,
        "solana_tvl_change_24h_pct": tvl_change_pct,
        "solana_dex_volume_24h_usd": dex_overview.get("total24h"),
        "solana_stablecoin_supply_usd": current_stablecoin_supply,
        "median_tx_fee_lamports": fee_estimate.get("median_fee_lamports"),
        "estimated_rev_usd_per_block": fee_estimate.get("estimated_rev_usd_per_block"),
    }


def ecosystem_growth(offchain: dict) -> dict:
    """
    Placeholders for metrics that don't have a single canonical keyless
    feed yet (tokenized equities volume, daily active addresses). Wired
    up as an explicit, documented gap rather than a fabricated number —
    see README "Ecosystem growth data gaps" for exactly what's needed
    to fill these in (e.g. a Dune API key for a specific dashboard).
    """
    return {
        "tokenized_equities_volume_usd": None,
        "daily_active_addresses": None,
        "note": (
            "Both metrics require either a Dune Analytics API key tied to a "
            "specific dashboard, or a paid indexer — no keyless public "
            "endpoint currently covers Solana-wide tokenized RWA volume or "
            "unique daily active addresses. See README for how to wire in "
            "a Dune API key if you have one."
        ),
    }
