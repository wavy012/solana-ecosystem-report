# Solana Ecosystem Report
_Generated 2026-11-27T18:38:33+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 474,653,579 |
| Current epoch | 1,098 |
| Epoch progress | 73.51% |
| Avg TPS (recent) | 2,007.15 |
| Max TPS (recent) | 2,403.0 |
| Avg slot time | 213.39 ms |
| Cluster health | ok |

## Validator status

- Active validators: **654**
- Delinquent validators: **34**
- Delinquency rate: **4.94%**
- Total active stake: **424,207,451.2 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 16,815,245.1 | 3.964% | 0% |
| 2 | `CcaHc2L4…` | 15,826,051.59 | 3.731% | 7% |
| 3 | `3N7s9zXM…` | 12,437,387.71 | 2.932% | 0% |
| 4 | `8GbwASqd…` | 10,238,108.01 | 2.413% | 0% |
| 5 | `51JBzSTU…` | 9,920,637.35 | 2.339% | 10% |
| 6 | `CatzoSMU…` | 9,617,109.17 | 2.267% | 5% |
| 7 | `26pV97Ce…` | 9,296,651.24 | 2.192% | 7% |
| 8 | `9QU2QSxh…` | 8,037,877.4 | 1.895% | 7% |
| 9 | `DumiCKHV…` | 6,972,140.88 | 1.644% | 0% |
| 10 | `CvSb7wdQ…` | 6,741,351.36 | 1.589% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $71.77 |
| 24h price change | 0.81% |
| Market cap | $42,503,327,953.28923 |
| 24h volume | $2,760,608,198.58137 |
| Solana TVL | $4,606,916,904 |
| TVL 24h change | 0.56% |
| DEX volume (24h) | $870,578,806.1700001 |
| Stablecoin supply | $12,720,038,168.230001 |
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