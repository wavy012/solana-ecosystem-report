# Solana Ecosystem Report
_Generated 2026-10-03T09:20:12+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 452,891,194 |
| Current epoch | 1,048 |
| Epoch progress | 35.92% |
| Avg TPS (recent) | 3,805.31 |
| Max TPS (recent) | 4,038.62 |
| Avg slot time | 265.67 ms |
| Cluster health | ok |

## Validator status

- Active validators: **672**
- Delinquent validators: **12**
- Delinquency rate: **1.75%**
- Total active stake: **442,013,190.17 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,923,954.11 | 4.055% | 7% |
| 2 | `he1iusun…` | 15,898,893.7 | 3.597% | 0% |
| 3 | `3N7s9zXM…` | 12,338,401.44 | 2.791% | 0% |
| 4 | `8GbwASqd…` | 11,304,108.22 | 2.557% | 0% |
| 5 | `CatzoSMU…` | 11,133,144.84 | 2.519% | 5% |
| 6 | `26pV97Ce…` | 9,247,323.71 | 2.092% | 7% |
| 7 | `51JBzSTU…` | 9,244,926.26 | 2.092% | 10% |
| 8 | `9QU2QSxh…` | 7,605,152.59 | 1.721% | 7% |
| 9 | `CvSb7wdQ…` | 7,060,360.59 | 1.597% | 5% |
| 10 | `3JD3jMmn…` | 6,684,212.68 | 1.512% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $119.37 |
| 24h price change | -2.16% |
| Market cap | $70,216,061,583.46056 |
| 24h volume | $3,241,977,734.634158 |
| Solana TVL | $6,642,005,967 |
| TVL 24h change | 1.02% |
| DEX volume (24h) | $2,569,613,456.96 |
| Stablecoin supply | $16,929,353,787.1 |
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