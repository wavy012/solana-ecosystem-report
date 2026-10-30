# Solana Ecosystem Report
_Generated 2026-10-30T02:48:38+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 463,122,172 |
| Current epoch | 1,072 |
| Epoch progress | 4.21% |
| Avg TPS (recent) | 1,849.02 |
| Max TPS (recent) | 2,239.17 |
| Avg slot time | 214.21 ms |
| Cluster health | ok |

## Validator status

- Active validators: **666**
- Delinquent validators: **25**
- Delinquency rate: **3.62%**
- Total active stake: **435,357,093.15 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 16,965,455.7 | 3.897% | 7% |
| 2 | `he1iusun…` | 16,678,000.07 | 3.831% | 0% |
| 3 | `3N7s9zXM…` | 12,919,679.96 | 2.968% | 0% |
| 4 | `8GbwASqd…` | 10,502,229.13 | 2.412% | 0% |
| 5 | `CatzoSMU…` | 9,659,910.32 | 2.219% | 5% |
| 6 | `51JBzSTU…` | 9,473,552.2 | 2.176% | 10% |
| 7 | `26pV97Ce…` | 9,222,405.53 | 2.118% | 7% |
| 8 | `9QU2QSxh…` | 7,780,140.24 | 1.787% | 7% |
| 9 | `CvSb7wdQ…` | 7,045,149.57 | 1.618% | 5% |
| 10 | `DumiCKHV…` | 7,001,505.63 | 1.608% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.17 |
| 24h price change | -4.42% |
| Market cap | $56,137,340,429.8734 |
| 24h volume | $5,267,763,942.954862 |
| Solana TVL | $5,354,098,163 |
| TVL 24h change | -4.2% |
| DEX volume (24h) | $1,924,354,203.6999998 |
| Stablecoin supply | $15,459,786,777.66 |
| Median tx fee | — |
| Est. REV / block | $— |

## Ecosystem growth

- Tokenized equities volume: —
- Daily active addresses: —

> Both metrics require either a Dune Analytics API key tied to a specific dashboard, or a paid indexer — no keyless public endpoint currently covers Solana-wide tokenized RWA volume or unique daily active addresses. See README for how to wire in a Dune API key if you have one.

## Upcoming upgrades & developments

- **Alpenglow** — _In community review / staged rollout_ — Proposed consensus overhaul (Votor + Rotor) targeting ~100-150ms finality, replacing PoH/Tower BFT.
- **SIMD-0225 (Alpenglow governance proposal)** — _Tracking validator vote_ — On-chain validator vote to approve the Alpenglow consensus change.
- **Fee market / SIMD proposals** — _Varies — check solana.com/news for the latest_ — Ongoing proposals adjusting local fee markets and priority fee mechanics.

## Sources unavailable this run

- `demo_address_balance`: RPC error calling getBalance: {'code': -32602, 'message': 'Invalid param: WrongSize'}
- `demo_address_recent_signatures`: RPC error calling getSignaturesForAddress: {'code': -32602, 'message': 'Invalid param: WrongSize'}
- `sample_block`: RPC error calling getBlock: {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}

---
_Generated automatically by the Solana Ecosystem Report pipeline. Data sources: Solana public RPC, DeFiLlama, CoinGecko._