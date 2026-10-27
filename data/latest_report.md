# Solana Ecosystem Report
_Generated 2026-10-27T07:11:09+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 461,980,986 |
| Current epoch | 1,069 |
| Epoch progress | 40.04% |
| Avg TPS (recent) | 1,232.8 |
| Max TPS (recent) | 1,553.13 |
| Avg slot time | 212.69 ms |
| Cluster health | ok |

## Validator status

- Active validators: **665**
- Delinquent validators: **20**
- Delinquency rate: **2.92%**
- Total active stake: **436,873,593.07 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,059,304.44 | 3.905% | 7% |
| 2 | `he1iusun…` | 16,636,452.76 | 3.808% | 0% |
| 3 | `3N7s9zXM…` | 12,660,116.86 | 2.898% | 0% |
| 4 | `8GbwASqd…` | 10,812,576.74 | 2.475% | 0% |
| 5 | `CatzoSMU…` | 9,716,980.31 | 2.224% | 5% |
| 6 | `51JBzSTU…` | 9,494,053.09 | 2.173% | 10% |
| 7 | `26pV97Ce…` | 9,206,551.54 | 2.107% | 7% |
| 8 | `9QU2QSxh…` | 7,754,188.75 | 1.775% | 7% |
| 9 | `CvSb7wdQ…` | 7,040,177.16 | 1.611% | 5% |
| 10 | `DumiCKHV…` | 6,996,375.0 | 1.601% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $99.53 |
| 24h price change | -1.36% |
| Market cap | $58,709,296,741.19727 |
| 24h volume | $2,329,713,792.6043224 |
| Solana TVL | $5,687,726,706 |
| TVL 24h change | -0.28% |
| DEX volume (24h) | $1,715,654,561.15 |
| Stablecoin supply | $15,775,671,641.46 |
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