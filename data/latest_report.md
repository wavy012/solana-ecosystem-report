# Solana Ecosystem Report
_Generated 2026-11-04T07:10:27+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 465,212,951 |
| Current epoch | 1,076 |
| Epoch progress | 88.18% |
| Avg TPS (recent) | 1,435.86 |
| Max TPS (recent) | 1,744.33 |
| Avg slot time | 214.3 ms |
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
| SOL price | $92.74 |
| 24h price change | 1.29% |
| Market cap | $54,695,106,549.985435 |
| 24h volume | $2,622,949,266.154313 |
| Solana TVL | $5,370,839,896 |
| TVL 24h change | -0.54% |
| DEX volume (24h) | $1,873,449,588.9 |
| Stablecoin supply | $15,050,364,888.109999 |
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