# Solana Ecosystem Report
_Generated 2026-11-20T03:49:42+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 471,592,426 |
| Current epoch | 1,091 |
| Epoch progress | 64.91% |
| Avg TPS (recent) | 1,715.37 |
| Max TPS (recent) | 2,272.07 |
| Avg slot time | 215.55 ms |
| Cluster health | ok |

## Validator status

- Active validators: **659**
- Delinquent validators: **26**
- Delinquency rate: **3.8%**
- Total active stake: **428,682,730.45 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 17,028,959.52 | 3.972% | 0% |
| 2 | `CcaHc2L4…` | 16,375,744.56 | 3.82% | 7% |
| 3 | `3N7s9zXM…` | 12,422,024.76 | 2.898% | 0% |
| 4 | `8GbwASqd…` | 10,299,570.28 | 2.403% | 0% |
| 5 | `51JBzSTU…` | 9,815,430.79 | 2.29% | 10% |
| 6 | `CatzoSMU…` | 9,573,247.98 | 2.233% | 5% |
| 7 | `26pV97Ce…` | 9,225,577.82 | 2.152% | 7% |
| 8 | `9QU2QSxh…` | 7,980,783.98 | 1.862% | 7% |
| 9 | `DumiCKHV…` | 6,997,844.19 | 1.632% | 0% |
| 10 | `CvSb7wdQ…` | 6,772,455.16 | 1.58% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $72.86 |
| 24h price change | -1.63% |
| Market cap | $43,119,773,836.238396 |
| 24h volume | $2,481,067,349.9659915 |
| Solana TVL | $4,702,402,454 |
| TVL 24h change | -0.22% |
| DEX volume (24h) | $1,847,338,570.06 |
| Stablecoin supply | $13,483,840,863.3 |
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