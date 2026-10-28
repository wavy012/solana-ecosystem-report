# Solana Ecosystem Report
_Generated 2026-10-28T08:03:43+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 462,401,712 |
| Current epoch | 1,070 |
| Epoch progress | 37.43% |
| Avg TPS (recent) | 1,290.92 |
| Max TPS (recent) | 1,583.7 |
| Avg slot time | 212.85 ms |
| Cluster health | ok |

## Validator status

- Active validators: **662**
- Delinquent validators: **29**
- Delinquency rate: **4.2%**
- Total active stake: **437,290,026.34 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,006,421.92 | 3.889% | 7% |
| 2 | `he1iusun…` | 16,661,096.44 | 3.81% | 0% |
| 3 | `3N7s9zXM…` | 12,791,931.11 | 2.925% | 0% |
| 4 | `8GbwASqd…` | 10,815,143.08 | 2.473% | 0% |
| 5 | `CatzoSMU…` | 9,718,548.06 | 2.222% | 5% |
| 6 | `51JBzSTU…` | 9,464,442.57 | 2.164% | 10% |
| 7 | `26pV97Ce…` | 9,208,877.3 | 2.106% | 7% |
| 8 | `9QU2QSxh…` | 7,757,994.43 | 1.774% | 7% |
| 9 | `CvSb7wdQ…` | 7,041,145.74 | 1.61% | 5% |
| 10 | `DumiCKHV…` | 6,997,044.02 | 1.6% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $102.24 |
| 24h price change | 2.25% |
| Market cap | $60,307,512,862.16228 |
| 24h volume | $1,907,097,968.145909 |
| Solana TVL | $5,728,613,237 |
| TVL 24h change | 1.04% |
| DEX volume (24h) | $1,848,987,960.5499997 |
| Stablecoin supply | $15,791,603,551.359999 |
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