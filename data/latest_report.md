# Solana Ecosystem Report
_Generated 2026-11-04T00:44:52+00:00_

## Anomalies

- **[WARNING]** TPS spike: 2368.21 vs rolling baseline 1569.62 (50.9%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 465,104,842 |
| Current epoch | 1,076 |
| Epoch progress | 63.16% |
| Avg TPS (recent) | 2,368.21 |
| Max TPS (recent) | 2,785.32 |
| Avg slot time | 214.14 ms |
| Cluster health | ok |

## Validator status

- Active validators: **666**
- Delinquent validators: **27**
- Delinquency rate: **3.9%**
- Total active stake: **434,699,176.96 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,030,640.79 | 3.918% | 7% |
| 2 | `he1iusun…` | 16,704,339.56 | 3.843% | 0% |
| 3 | `3N7s9zXM…` | 13,043,664.46 | 3.001% | 0% |
| 4 | `8GbwASqd…` | 10,431,126.13 | 2.4% | 0% |
| 5 | `CatzoSMU…` | 9,561,007.3 | 2.199% | 5% |
| 6 | `51JBzSTU…` | 9,435,904.6 | 2.171% | 10% |
| 7 | `26pV97Ce…` | 9,232,746.39 | 2.124% | 7% |
| 8 | `9QU2QSxh…` | 7,814,809.95 | 1.798% | 7% |
| 9 | `DumiCKHV…` | 7,008,985.64 | 1.612% | 0% |
| 10 | `CvSb7wdQ…` | 6,979,030.58 | 1.605% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $91.77 |
| 24h price change | -0.59% |
| Market cap | $54,177,572,842.369484 |
| 24h volume | $2,059,997,809.3517337 |
| Solana TVL | $5,446,096,870 |
| TVL 24h change | -0.22% |
| DEX volume (24h) | $1,809,611,297.5 |
| Stablecoin supply | $15,525,004,037.93 |
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