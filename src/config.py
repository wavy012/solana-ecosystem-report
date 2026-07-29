"""
Central configuration for the Solana Ecosystem Report.

Everything here can be overridden with environment variables so the
pipeline can run with zero required API keys, while still letting a
power user plug in a private RPC endpoint (Helius/Triton/etc.) for
higher rate limits if they have one.
"""
import os

# --- Solana RPC -------------------------------------------------------
# Public, keyless mainnet-beta endpoint. Swap via SOLANA_RPC_URL env var
# if you have a private RPC provider (recommended for production use —
# the public endpoint is rate limited).
SOLANA_RPC_URL = os.environ.get("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")

# Address used for the getBalance / getSignaturesForAddress demo calls.
# Defaults to the native System Program (always exists, always safe to
# query). Override with SOLANA_DEMO_ADDRESS to track a specific wallet,
# multisig, or program.
SOLANA_DEMO_ADDRESS = os.environ.get("SOLANA_DEMO_ADDRESS", "11111111111111111111111111111111111111112")

RPC_TIMEOUT_SECONDS = 10

# --- Off-chain data sources -------------------------------------------
DEFILLAMA_CHAIN_TVL_URL = "https://api.llama.fi/v2/historicalChainTvl/Solana"
DEFILLAMA_DEX_OVERVIEW_URL = "https://api.llama.fi/overview/dexs/solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true"
DEFILLAMA_STABLECOIN_URL = "https://stablecoins.llama.fi/stablecoincharts/Solana"
COINGECKO_PRICE_URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=solana&vs_currencies=usd&include_market_cap=true"
    "&include_24hr_vol=true&include_24hr_change=true"
)

HTTP_TIMEOUT_SECONDS = 15
HTTP_USER_AGENT = "solana-ecosystem-report/1.0 (+https://github.com/)"

# --- Automation ---------------------------------------------------------
# How often (seconds) the pipeline refreshes when run with --loop.
# Overridden with REPORT_REFRESH_SECONDS. Default: 15 minutes.
REFRESH_INTERVAL_SECONDS = int(os.environ.get("REPORT_REFRESH_SECONDS", 900))

# How many historical snapshots to retain for trend charts + anomaly
# baselines. At the default 15-minute interval, 200 snapshots is ~2 days.
HISTORY_MAX_SNAPSHOTS = int(os.environ.get("REPORT_HISTORY_MAX", 200))

# --- Anomaly detection thresholds ---------------------------------------
# Each is a simple, explainable rule rather than a black box, so judges
# and users can see exactly why something fired.
ANOMALY_THRESHOLDS = {
    # % deviation from the rolling mean of the last N snapshots
    "tps_deviation_pct": 30,
    "slot_time_ms_max": 550,          # Solana's target slot time is ~400ms
    "validator_delinquency_pct_max": 5,
    "tvl_change_pct_24h": 15,
    "sol_price_change_pct_24h": 10,
}
ANOMALY_ROLLING_WINDOW = 20  # snapshots used to compute the rolling baseline

# --- Output paths ---------------------------------------------------------
DATA_DIR = "data"
DOCS_DIR = "docs"  # docs/ so GitHub Pages can serve straight from this folder
HISTORY_FILE = os.path.join(DATA_DIR, "history.jsonl")
LATEST_JSON = os.path.join(DATA_DIR, "latest_report.json")
LATEST_MD = os.path.join(DATA_DIR, "latest_report.md")
DASHBOARD_HTML = os.path.join(DOCS_DIR, "index.html")

# Upcoming protocol developments to surface in the report. This is the
# one section that's manually curated rather than pulled live, since
# there's no single canonical keyless feed for Solana Improvement
# Document (SIMD) status. Update this list as things progress —
# see README.md "Keeping the roadmap section current".
UPCOMING_DEVELOPMENTS = [
    {
        "name": "Alpenglow",
        "summary": "Proposed consensus overhaul (Votor + Rotor) targeting ~100-150ms finality, replacing PoH/Tower BFT.",
        "status": "In community review / staged rollout",
    },
    {
        "name": "SIMD-0225 (Alpenglow governance proposal)",
        "summary": "On-chain validator vote to approve the Alpenglow consensus change.",
        "status": "Tracking validator vote",
    },
    {
        "name": "Fee market / SIMD proposals",
        "summary": "Ongoing proposals adjusting local fee markets and priority fee mechanics.",
        "status": "Varies — check solana.com/news for the latest",
    },
]
