# Solana Ecosystem Report
_Generated 2026-10-06T23:30:30+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 454,048,914 |
| Current epoch | 1,051 |
| Epoch progress | 3.91% |
| Avg TPS (recent) | 4,731.83 |
| Max TPS (recent) | 5,138.72 |
| Avg slot time | 269.92 ms |
| Cluster health | ok |

## Validator status

- Active validators: **673**
- Delinquent validators: **8**
- Delinquency rate: **1.17%**
- Total active stake: **439,343,030.7 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,653,054.75 | 4.018% | 7% |
| 2 | `he1iusun…` | 15,968,868.81 | 3.635% | 0% |
| 3 | `3N7s9zXM…` | 12,308,200.7 | 2.802% | 0% |
| 4 | `8GbwASqd…` | 11,264,080.77 | 2.564% | 0% |
| 5 | `CatzoSMU…` | 11,149,017.24 | 2.538% | 5% |
| 6 | `26pV97Ce…` | 9,259,685.35 | 2.108% | 7% |
| 7 | `51JBzSTU…` | 9,251,538.37 | 2.106% | 10% |
| 8 | `9QU2QSxh…` | 7,508,702.81 | 1.709% | 7% |
| 9 | `CvSb7wdQ…` | 7,113,963.23 | 1.619% | 5% |
| 10 | `3JD3jMmn…` | 6,690,032.29 | 1.523% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $120.6 |
| 24h price change | -0.17% |
| Market cap | $70,965,371,725.95332 |
| 24h volume | $2,455,305,931.18911 |
| Solana TVL | $6,624,348,948 |
| TVL 24h change | -0.06% |
| DEX volume (24h) | $2,057,146,062.5000002 |
| Stablecoin supply | $17,029,824,007.73 |
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