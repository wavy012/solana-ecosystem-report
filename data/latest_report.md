# Solana Ecosystem Report
_Generated 2026-11-17T08:44:44+00:00_

## Anomalies

- **[WARNING]** TPS drop: 1080.75 vs rolling baseline 1782.5 (-39.4%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 470,471,263 |
| Current epoch | 1,089 |
| Epoch progress | 5.38% |
| Avg TPS (recent) | 1,080.75 |
| Max TPS (recent) | 1,351.02 |
| Avg slot time | 214.96 ms |
| Cluster health | ok |

## Validator status

- Active validators: **661**
- Delinquent validators: **5**
- Delinquency rate: **0.75%**
- Total active stake: **428,796,575.89 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 16,834,343.15 | 3.926% | 0% |
| 2 | `CcaHc2L4…` | 16,442,667.55 | 3.835% | 7% |
| 3 | `3N7s9zXM…` | 12,432,777.89 | 2.899% | 0% |
| 4 | `8GbwASqd…` | 10,144,846.19 | 2.366% | 0% |
| 5 | `51JBzSTU…` | 9,802,677.35 | 2.286% | 10% |
| 6 | `CatzoSMU…` | 9,625,020.62 | 2.245% | 5% |
| 7 | `26pV97Ce…` | 9,218,744.86 | 2.15% | 7% |
| 8 | `9QU2QSxh…` | 7,970,890.85 | 1.859% | 7% |
| 9 | `DumiCKHV…` | 6,996,288.22 | 1.632% | 0% |
| 10 | `CvSb7wdQ…` | 6,730,472.2 | 1.57% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $72.29 |
| 24h price change | 1.82% |
| Market cap | $42,769,775,137.446495 |
| 24h volume | $2,725,687,593.091054 |
| Solana TVL | $4,765,531,754 |
| TVL 24h change | 1.69% |
| DEX volume (24h) | $1,397,954,142.31 |
| Stablecoin supply | $14,364,284,258.83 |
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