# Solana Ecosystem Report
_Generated 2026-10-24T09:42:14+00:00_

## Anomalies

- **[WARNING]** TPS drop: 1480.4 vs rolling baseline 2625.58 (-43.6%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 460,803,288 |
| Current epoch | 1,066 |
| Epoch progress | 67.43% |
| Avg TPS (recent) | 1,480.4 |
| Max TPS (recent) | 1,970.13 |
| Avg slot time | 212.56 ms |
| Cluster health | ok |

## Validator status

- Active validators: **664**
- Delinquent validators: **14**
- Delinquency rate: **2.06%**
- Total active stake: **437,116,781.97 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,096,229.98 | 3.911% | 7% |
| 2 | `he1iusun…` | 16,022,777.9 | 3.666% | 0% |
| 3 | `3N7s9zXM…` | 12,572,396.11 | 2.876% | 0% |
| 4 | `8GbwASqd…` | 10,882,510.65 | 2.49% | 0% |
| 5 | `CatzoSMU…` | 9,724,045.66 | 2.225% | 5% |
| 6 | `51JBzSTU…` | 9,478,407.19 | 2.168% | 10% |
| 7 | `26pV97Ce…` | 9,213,418.49 | 2.108% | 7% |
| 8 | `9QU2QSxh…` | 7,782,538.8 | 1.78% | 7% |
| 9 | `CvSb7wdQ…` | 7,037,301.09 | 1.61% | 5% |
| 10 | `DumiCKHV…` | 7,003,144.98 | 1.602% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $101.22 |
| 24h price change | -2.58% |
| Market cap | $59,653,026,396.263 |
| 24h volume | $2,278,615,338.170591 |
| Solana TVL | $5,755,562,537 |
| TVL 24h change | -1.81% |
| DEX volume (24h) | $2,020,963,434.3700001 |
| Stablecoin supply | $15,929,984,083.619999 |
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