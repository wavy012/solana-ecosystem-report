"""
Direct Solana JSON-RPC calls — no SDK, no API key, just stdlib HTTP.

Every function returns plain Python data (dicts/lists/numbers) already
shaped for the report builder. Each call is wrapped so a single failing
method (rate limit, timeout) degrades gracefully instead of crashing the
whole pipeline — the report notes which sections were unavailable this run.
"""
from . import config
from .http_client import post_json_rpc, FetchError


def _safe(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs), None
    except FetchError as e:
        return None, str(e)


def get_slot():
    return post_json_rpc(config.SOLANA_RPC_URL, "getSlot", [{"commitment": "confirmed"}])


def get_block_time(slot: int):
    return post_json_rpc(config.SOLANA_RPC_URL, "getBlockTime", [slot])


def get_epoch_info():
    return post_json_rpc(config.SOLANA_RPC_URL, "getEpochInfo", [])


def get_recent_performance_samples(limit: int = 30):
    return post_json_rpc(config.SOLANA_RPC_URL, "getRecentPerformanceSamples", [limit])


def get_vote_accounts():
    return post_json_rpc(config.SOLANA_RPC_URL, "getVoteAccounts", [])


def get_balance(pubkey: str):
    result = post_json_rpc(config.SOLANA_RPC_URL, "getBalance", [pubkey])
    return result.get("value") if isinstance(result, dict) else result


def get_signatures_for_address(pubkey: str, limit: int = 10):
    return post_json_rpc(config.SOLANA_RPC_URL, "getSignaturesForAddress", [pubkey, {"limit": limit}])


def get_health():
    try:
        return post_json_rpc(config.SOLANA_RPC_URL, "getHealth", [])
    except FetchError as e:
        # getHealth returns a JSON-RPC *error* body (not HTTP error) when unhealthy,
        # which our post_json_rpc treats as a FetchError. Surface it as a status string.
        return f"unhealthy: {e}"


def get_supply():
    return post_json_rpc(config.SOLANA_RPC_URL, "getSupply", [{"excludeNonCirculatingAccountsList": True}])


def get_block(slot: int):
    """
    Full block with transaction metadata, used to derive real median
    transaction fees (base + priority) directly from on-chain data
    instead of guessing a flat 5000-lamport base fee.
    """
    return post_json_rpc(config.SOLANA_RPC_URL, "getBlock", [slot, {
        "encoding": "json",
        "transactionDetails": "full",
        "maxSupportedTransactionVersion": 0,
        "rewards": False,
    }])


def collect_onchain_snapshot() -> dict:
    """
    Pulls every on-chain metric the bounty asks for in one pass.
    Returns a dict with a `data` key per metric and an `errors` key
    listing anything that failed, so the caller can still emit a
    partial report instead of failing outright.
    """
    errors = {}
    data = {}

    slot, err = _safe(get_slot)
    data["slot"] = slot
    if err:
        errors["slot"] = err

    epoch_info, err = _safe(get_epoch_info)
    data["epoch_info"] = epoch_info
    if err:
        errors["epoch_info"] = err

    perf_samples, err = _safe(get_recent_performance_samples, 30)
    data["performance_samples"] = perf_samples
    if err:
        errors["performance_samples"] = err

    vote_accounts, err = _safe(get_vote_accounts)
    data["vote_accounts"] = vote_accounts
    if err:
        errors["vote_accounts"] = err

    health, err = _safe(get_health)
    data["health"] = health
    if err:
        errors["health"] = err

    supply, err = _safe(get_supply)
    data["supply"] = supply
    if err:
        errors["supply"] = err

    balance, err = _safe(get_balance, config.SOLANA_DEMO_ADDRESS)
    data["demo_address_balance_lamports"] = balance
    if err:
        errors["demo_address_balance"] = err

    signatures, err = _safe(get_signatures_for_address, config.SOLANA_DEMO_ADDRESS, 10)
    data["demo_address_recent_signatures"] = signatures
    if err:
        errors["demo_address_recent_signatures"] = err

    block_time = None
    if slot:
        block_time, err = _safe(get_block_time, slot)
        if err:
            errors["block_time"] = err
    data["latest_block_time"] = block_time

    # Sample a recent, already-finalized block for real fee data.
    # We step back a bit from the tip since getBlock requires the slot
    # to be finalized/rooted, which the very latest confirmed slot may not be yet.
    sample_block = None
    if slot:
        sample_block, err = _safe(get_block, max(slot - 50, 0))
        if err:
            errors["sample_block"] = err
    data["sample_block"] = sample_block

    data["_errors"] = errors
    return data
