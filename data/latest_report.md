# Solana Ecosystem Report
_Generated 2026-10-10T12:49:34+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 455,261,400 |
| Current epoch | 1,053 |
| Epoch progress | 84.58% |
| Avg TPS (recent) | 4,460.4 |
| Max TPS (recent) | 4,831.82 |
| Avg slot time | 218.24 ms |
| Cluster health | ok |

## Validator status

- Active validators: **675**
- Delinquent validators: **6**
- Delinquency rate: **0.88%**
- Total active stake: **437,867,726.51 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,788,627.2 | 4.063% | 7% |
| 2 | `he1iusun…` | 15,954,194.79 | 3.644% | 0% |
| 3 | `3N7s9zXM…` | 12,299,759.25 | 2.809% | 0% |
| 4 | `8GbwASqd…` | 11,178,786.74 | 2.553% | 0% |
| 5 | `CatzoSMU…` | 10,972,769.54 | 2.506% | 5% |
| 6 | `51JBzSTU…` | 9,315,835.37 | 2.128% | 10% |
| 7 | `26pV97Ce…` | 9,251,552.15 | 2.113% | 7% |
| 8 | `9QU2QSxh…` | 7,589,921.71 | 1.733% | 7% |
| 9 | `CvSb7wdQ…` | 6,809,494.18 | 1.555% | 5% |
| 10 | `3JD3jMmn…` | 6,692,115.38 | 1.528% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $109.63 |
| 24h price change | -0.6% |
| Market cap | $64,550,164,684.75762 |
| 24h volume | $2,023,730,500.8403268 |
| Solana TVL | $6,201,832,526 |
| TVL 24h change | -0.16% |
| DEX volume (24h) | $1,978,097,665.9099998 |
| Stablecoin supply | $16,409,904,507.15 |
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