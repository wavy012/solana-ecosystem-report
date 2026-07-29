"""
Off-chain / ecosystem data sources.

DeFiLlama and CoinGecko both expose keyless public endpoints, which is
why they're used here instead of paid data providers. Twitter/X is
intentionally NOT wired up automatically: the current X API requires a
paid bearer token, which would violate the bounty's "no API keys"
preference for anyone who doesn't already have one. See README.md
"Twitter/X integration" for how to plug it in optionally.
"""
from . import config
from .http_client import get_json, FetchError


def _safe(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs), None
    except FetchError as e:
        return None, str(e)


def get_solana_tvl_history():
    """Historical + current Solana TVL from DeFiLlama (USD)."""
    return get_json(config.DEFILLAMA_CHAIN_TVL_URL)


def get_solana_dex_overview():
    """24h DEX volume aggregated across Solana DEXs, from DeFiLlama."""
    return get_json(config.DEFILLAMA_DEX_OVERVIEW_URL)


def get_solana_stablecoin_supply():
    """Stablecoin supply on Solana over time, from DeFiLlama."""
    return get_json(config.DEFILLAMA_STABLECOIN_URL)


def get_sol_price():
    """Spot price, market cap, 24h volume, 24h change from CoinGecko."""
    return get_json(config.COINGECKO_PRICE_URL)


def collect_offchain_snapshot() -> dict:
    errors = {}
    data = {}

    tvl_history, err = _safe(get_solana_tvl_history)
    data["tvl_history"] = tvl_history
    if err:
        errors["tvl_history"] = err

    dex_overview, err = _safe(get_solana_dex_overview)
    data["dex_overview"] = dex_overview
    if err:
        errors["dex_overview"] = err

    stablecoins, err = _safe(get_solana_stablecoin_supply)
    data["stablecoin_supply"] = stablecoins
    if err:
        errors["stablecoin_supply"] = err

    price, err = _safe(get_sol_price)
    data["sol_price"] = price
    if err:
        errors["sol_price"] = err

    data["_errors"] = errors
    return data
