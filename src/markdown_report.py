"""Renders the human-readable Markdown report from the same report dict as the JSON/HTML outputs."""


def _fmt(v, suffix="", dash="—"):
    if v is None:
        return dash
    return f"{v:,}{suffix}" if isinstance(v, (int, float)) else f"{v}{suffix}"


def render_markdown(report: dict) -> str:
    perf = report.get("network_performance", {})
    validators = report.get("validator_status", {})
    econ = report.get("economic_indicators", {})
    growth = report.get("ecosystem_growth", {})
    anomalies = report.get("anomalies", [])
    roadmap = report.get("upcoming_developments", [])
    errors = report.get("source_errors", {})

    lines = []
    lines.append(f"# Solana Ecosystem Report")
    lines.append(f"_Generated {report.get('generated_at_utc', '')}_\n")

    lines.append("## Anomalies\n")
    if anomalies:
        for a in anomalies:
            lines.append(f"- **[{a['severity'].upper()}]** {a['message']}")
    else:
        lines.append("- No metric breached its threshold this run.")
    lines.append("")

    lines.append("## Network performance\n")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| Current slot | {_fmt(perf.get('current_slot'))} |")
    lines.append(f"| Current epoch | {_fmt(perf.get('current_epoch'))} |")
    lines.append(f"| Epoch progress | {_fmt(perf.get('epoch_progress_pct'), '%')} |")
    lines.append(f"| Avg TPS (recent) | {_fmt(perf.get('avg_tps_recent'))} |")
    lines.append(f"| Max TPS (recent) | {_fmt(perf.get('max_tps_recent'))} |")
    lines.append(f"| Avg slot time | {_fmt(perf.get('avg_slot_time_ms'), ' ms')} |")
    lines.append(f"| Cluster health | {_fmt(perf.get('cluster_health'))} |")
    lines.append("")

    lines.append("## Validator status\n")
    lines.append(f"- Active validators: **{_fmt(validators.get('active_validator_count'))}**")
    lines.append(f"- Delinquent validators: **{_fmt(validators.get('delinquent_validator_count'))}**")
    lines.append(f"- Delinquency rate: **{_fmt(validators.get('delinquency_pct'), '%')}**")
    lines.append(f"- Total active stake: **{_fmt(validators.get('total_active_stake_sol'), ' SOL')}**")
    lines.append(f"- Median commission: **{_fmt(validators.get('median_commission_pct'), '%')}**")
    lines.append("")
    lines.append("### Top validators by stake\n")
    lines.append("| # | Vote account | Stake (SOL) | Share | Commission |")
    lines.append("|---|---|---|---|---|")
    for i, v in enumerate(validators.get("top_validators_by_stake", [])):
        lines.append(
            f"| {i+1} | `{(v.get('vote_pubkey') or '')[:8]}…` | {_fmt(v.get('activated_stake_sol'))} | "
            f"{_fmt(v.get('stake_share_pct'), '%')} | {_fmt(v.get('commission_pct'), '%')} |"
        )
    lines.append("")

    lines.append("## Economic indicators\n")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| SOL price | ${_fmt(econ.get('sol_price_usd'))} |")
    lines.append(f"| 24h price change | {_fmt(econ.get('sol_price_change_24h_pct'), '%')} |")
    lines.append(f"| Market cap | ${_fmt(econ.get('sol_market_cap_usd'))} |")
    lines.append(f"| 24h volume | ${_fmt(econ.get('sol_24h_volume_usd'))} |")
    lines.append(f"| Solana TVL | ${_fmt(econ.get('solana_tvl_usd'))} |")
    lines.append(f"| TVL 24h change | {_fmt(econ.get('solana_tvl_change_24h_pct'), '%')} |")
    lines.append(f"| DEX volume (24h) | ${_fmt(econ.get('solana_dex_volume_24h_usd'))} |")
    lines.append(f"| Stablecoin supply | ${_fmt(econ.get('solana_stablecoin_supply_usd'))} |")
    lines.append(f"| Median tx fee | {_fmt(econ.get('median_tx_fee_lamports'), ' lamports')} |")
    lines.append(f"| Est. REV / block | ${_fmt(econ.get('estimated_rev_usd_per_block'))} |")
    lines.append("")

    lines.append("## Ecosystem growth\n")
    lines.append(f"- Tokenized equities volume: {_fmt(growth.get('tokenized_equities_volume_usd'))}")
    lines.append(f"- Daily active addresses: {_fmt(growth.get('daily_active_addresses'))}")
    lines.append(f"\n> {growth.get('note', '')}\n")

    lines.append("## Upcoming upgrades & developments\n")
    for item in roadmap:
        lines.append(f"- **{item['name']}** — _{item['status']}_ — {item['summary']}")
    lines.append("")

    if errors:
        lines.append("## Sources unavailable this run\n")
        for k, v in errors.items():
            lines.append(f"- `{k}`: {v}")
        lines.append("")

    lines.append("---")
    lines.append("_Generated automatically by the Solana Ecosystem Report pipeline. "
                  "Data sources: Solana public RPC, DeFiLlama, CoinGecko._")

    return "\n".join(lines)
