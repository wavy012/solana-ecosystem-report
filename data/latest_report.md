# Solana Ecosystem Report
_Generated 2026-10-20T08:45:51+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 459,168,656 |
| Current epoch | 1,062 |
| Epoch progress | 89.03% |
| Avg TPS (recent) | 4,602.13 |
| Max TPS (recent) | 5,454.0 |
| Avg slot time | 217.81 ms |
| Cluster health | ok |

## Validator status

- Active validators: **668**
- Delinquent validators: **11**
- Delinquency rate: **1.62%**
- Total active stake: **437,880,622.23 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,095,414.59 | 3.904% | 7% |
| 2 | `he1iusun…` | 15,730,365.32 | 3.592% | 0% |
| 3 | `3N7s9zXM…` | 12,524,167.66 | 2.86% | 0% |
| 4 | `8GbwASqd…` | 10,975,835.74 | 2.507% | 0% |
| 5 | `CatzoSMU…` | 9,717,890.31 | 2.219% | 5% |
| 6 | `51JBzSTU…` | 9,481,609.09 | 2.165% | 10% |
| 7 | `26pV97Ce…` | 9,252,107.14 | 2.113% | 7% |
| 8 | `9QU2QSxh…` | 7,785,119.33 | 1.778% | 7% |
| 9 | `CvSb7wdQ…` | 6,993,888.17 | 1.597% | 5% |
| 10 | `DumiCKHV…` | 6,731,555.83 | 1.537% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.14 |
| 24h price change | -1.54% |
| Market cap | $61,391,254,424.50754 |
| 24h volume | $2,433,616,038.974679 |
| Solana TVL | $5,875,452,344 |
| TVL 24h change | 0.41% |
| DEX volume (24h) | $1,610,948,501.83 |
| Stablecoin supply | $15,915,085,718.82 |
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