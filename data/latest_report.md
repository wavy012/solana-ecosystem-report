# Solana Ecosystem Report
_Generated 2026-09-24T17:42:10+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 450,099,520 |
| Current epoch | 1,041 |
| Epoch progress | 89.7% |
| Avg TPS (recent) | 4,751.11 |
| Max TPS (recent) | 5,246.55 |
| Avg slot time | 266.94 ms |
| Cluster health | ok |

## Validator status

- Active validators: **674**
- Delinquent validators: **12**
- Delinquency rate: **1.75%**
- Total active stake: **439,964,136.84 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,843,203.19 | 4.056% | 7% |
| 2 | `he1iusun…` | 15,838,937.16 | 3.6% | 0% |
| 3 | `3N7s9zXM…` | 12,360,465.13 | 2.809% | 0% |
| 4 | `CatzoSMU…` | 11,264,812.27 | 2.56% | 5% |
| 5 | `8GbwASqd…` | 10,335,637.99 | 2.349% | 0% |
| 6 | `26pV97Ce…` | 9,226,124.27 | 2.097% | 7% |
| 7 | `51JBzSTU…` | 9,158,950.12 | 2.082% | 10% |
| 8 | `9QU2QSxh…` | 7,600,815.96 | 1.728% | 7% |
| 9 | `CvSb7wdQ…` | 7,090,584.89 | 1.612% | 5% |
| 10 | `DumiCKHV…` | 6,557,339.78 | 1.49% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $116.81 |
| 24h price change | 2.15% |
| Market cap | $68,665,456,933.14984 |
| 24h volume | $4,258,657,091.4158373 |
| Solana TVL | $6,411,040,784 |
| TVL 24h change | -1.89% |
| DEX volume (24h) | $2,552,816,117.41 |
| Stablecoin supply | $16,406,867,921.91 |
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