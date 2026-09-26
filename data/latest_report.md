# Solana Ecosystem Report
_Generated 2026-09-26T11:37:49+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 450,663,216 |
| Current epoch | 1,043 |
| Epoch progress | 20.18% |
| Avg TPS (recent) | 4,199.11 |
| Max TPS (recent) | 4,606.92 |
| Avg slot time | 268.3 ms |
| Cluster health | ok |

## Validator status

- Active validators: **676**
- Delinquent validators: **11**
- Delinquency rate: **1.6%**
- Total active stake: **437,542,654.24 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,860,284.36 | 4.082% | 7% |
| 2 | `he1iusun…` | 15,799,204.35 | 3.611% | 0% |
| 3 | `3N7s9zXM…` | 12,343,055.54 | 2.821% | 0% |
| 4 | `CatzoSMU…` | 11,222,560.6 | 2.565% | 5% |
| 5 | `8GbwASqd…` | 10,836,561.81 | 2.477% | 0% |
| 6 | `26pV97Ce…` | 9,237,101.73 | 2.111% | 7% |
| 7 | `51JBzSTU…` | 9,182,741.54 | 2.099% | 10% |
| 8 | `9QU2QSxh…` | 7,606,180.7 | 1.738% | 7% |
| 9 | `CvSb7wdQ…` | 7,093,311.0 | 1.621% | 5% |
| 10 | `DumiCKHV…` | 6,506,504.78 | 1.487% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $120.89 |
| 24h price change | -0.32% |
| Market cap | $71,084,303,411.77663 |
| 24h volume | $5,323,089,641.518829 |
| Solana TVL | $6,582,270,262 |
| TVL 24h change | 1.5% |
| DEX volume (24h) | $2,800,185,915.63 |
| Stablecoin supply | $16,970,475,445.460001 |
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