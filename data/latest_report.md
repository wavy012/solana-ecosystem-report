# Solana Ecosystem Report
_Generated 2026-10-17T02:36:33+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 457,872,647 |
| Current epoch | 1,059 |
| Epoch progress | 89.03% |
| Avg TPS (recent) | 4,594.28 |
| Max TPS (recent) | 5,126.25 |
| Avg slot time | 216.96 ms |
| Cluster health | ok |

## Validator status

- Active validators: **672**
- Delinquent validators: **9**
- Delinquency rate: **1.32%**
- Total active stake: **437,782,540.14 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,561,700.87 | 4.012% | 7% |
| 2 | `he1iusun…` | 15,460,528.28 | 3.532% | 0% |
| 3 | `3N7s9zXM…` | 12,362,554.93 | 2.824% | 0% |
| 4 | `8GbwASqd…` | 11,093,073.92 | 2.534% | 0% |
| 5 | `CatzoSMU…` | 10,200,312.46 | 2.33% | 5% |
| 6 | `51JBzSTU…` | 9,428,271.3 | 2.154% | 10% |
| 7 | `26pV97Ce…` | 9,248,874.25 | 2.113% | 7% |
| 8 | `9QU2QSxh…` | 7,743,557.36 | 1.769% | 7% |
| 9 | `CvSb7wdQ…` | 6,910,885.92 | 1.579% | 5% |
| 10 | `DumiCKHV…` | 6,417,147.83 | 1.466% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.18 |
| 24h price change | -1.09% |
| Market cap | $61,416,118,063.80142 |
| 24h volume | $2,884,225,925.115595 |
| Solana TVL | $5,928,129,415 |
| TVL 24h change | -0.89% |
| DEX volume (24h) | $1,921,414,372.11 |
| Stablecoin supply | $16,036,133,468.91 |
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