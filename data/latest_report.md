# Solana Ecosystem Report
_Generated 2026-10-22T21:06:26+00:00_

## Anomalies

- **[WARNING]** TPS drop: 2832.92 vs rolling baseline 4077.53 (-30.5%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 460,181,657 |
| Current epoch | 1,065 |
| Epoch progress | 23.53% |
| Avg TPS (recent) | 2,832.92 |
| Max TPS (recent) | 3,500.22 |
| Avg slot time | 213.03 ms |
| Cluster health | ok |

## Validator status

- Active validators: **655**
- Delinquent validators: **21**
- Delinquency rate: **3.11%**
- Total active stake: **438,318,925.5 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,133,144.03 | 3.909% | 7% |
| 2 | `he1iusun…` | 15,968,621.11 | 3.643% | 0% |
| 3 | `3N7s9zXM…` | 12,556,095.51 | 2.865% | 0% |
| 4 | `8GbwASqd…` | 10,936,236.81 | 2.495% | 0% |
| 5 | `CatzoSMU…` | 9,726,419.82 | 2.219% | 5% |
| 6 | `51JBzSTU…` | 9,476,173.66 | 2.162% | 10% |
| 7 | `26pV97Ce…` | 9,244,629.08 | 2.109% | 7% |
| 8 | `9QU2QSxh…` | 7,797,558.58 | 1.779% | 7% |
| 9 | `CvSb7wdQ…` | 7,036,292.6 | 1.605% | 5% |
| 10 | `DumiCKHV…` | 7,002,100.62 | 1.597% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.22 |
| 24h price change | -4.43% |
| Market cap | $60,863,185,835.72383 |
| 24h volume | $2,481,828,627.3760366 |
| Solana TVL | $5,856,931,364 |
| TVL 24h change | -1.82% |
| DEX volume (24h) | $2,270,402,206.37 |
| Stablecoin supply | $16,160,439,832.710001 |
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