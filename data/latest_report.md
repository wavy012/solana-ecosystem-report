# Solana Ecosystem Report
_Generated 2026-09-21T10:55:48+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 449,034,542 |
| Current epoch | 1,039 |
| Epoch progress | 43.17% |
| Avg TPS (recent) | 4,099.75 |
| Max TPS (recent) | 4,577.32 |
| Avg slot time | 266.18 ms |
| Cluster health | ok |

## Validator status

- Active validators: **677**
- Delinquent validators: **13**
- Delinquency rate: **1.88%**
- Total active stake: **439,905,518.63 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,856,583.01 | 4.059% | 7% |
| 2 | `he1iusun…` | 15,828,383.7 | 3.598% | 0% |
| 3 | `3N7s9zXM…` | 12,518,301.53 | 2.846% | 0% |
| 4 | `CatzoSMU…` | 11,252,587.79 | 2.558% | 5% |
| 5 | `8GbwASqd…` | 9,788,818.02 | 2.225% | 0% |
| 6 | `26pV97Ce…` | 9,251,354.09 | 2.103% | 7% |
| 7 | `51JBzSTU…` | 9,106,985.46 | 2.07% | 10% |
| 8 | `9QU2QSxh…` | 7,443,839.59 | 1.692% | 7% |
| 9 | `CvSb7wdQ…` | 7,088,079.33 | 1.611% | 5% |
| 10 | `DumiCKHV…` | 6,572,007.01 | 1.494% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $115.75 |
| 24h price change | 7.02% |
| Market cap | $67,994,344,454.979355 |
| 24h volume | $4,719,700,822.783997 |
| Solana TVL | $6,384,674,067 |
| TVL 24h change | 3.37% |
| DEX volume (24h) | $2,750,994,375.3599997 |
| Stablecoin supply | $15,885,472,242.89 |
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