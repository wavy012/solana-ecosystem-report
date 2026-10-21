# Solana Ecosystem Report
_Generated 2026-10-21T05:39:09+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 459,515,378 |
| Current epoch | 1,063 |
| Epoch progress | 69.29% |
| Avg TPS (recent) | 4,569.75 |
| Max TPS (recent) | 4,981.82 |
| Avg slot time | 216.14 ms |
| Cluster health | ok |

## Validator status

- Active validators: **668**
- Delinquent validators: **11**
- Delinquency rate: **1.62%**
- Total active stake: **438,577,211.11 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,103,015.5 | 3.9% | 7% |
| 2 | `he1iusun…` | 15,937,532.32 | 3.634% | 0% |
| 3 | `3N7s9zXM…` | 12,537,315.01 | 2.859% | 0% |
| 4 | `8GbwASqd…` | 10,930,433.98 | 2.492% | 0% |
| 5 | `CatzoSMU…` | 9,717,706.89 | 2.216% | 5% |
| 6 | `51JBzSTU…` | 9,482,036.87 | 2.162% | 10% |
| 7 | `26pV97Ce…` | 9,253,755.57 | 2.11% | 7% |
| 8 | `9QU2QSxh…` | 7,792,209.86 | 1.777% | 7% |
| 9 | `CvSb7wdQ…` | 7,034,137.56 | 1.604% | 5% |
| 10 | `DumiCKHV…` | 7,000,330.6 | 1.596% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.92 |
| 24h price change | 1.3% |
| Market cap | $62,440,120,178.022995 |
| 24h volume | $2,608,473,763.5848303 |
| Solana TVL | $5,950,205,637 |
| TVL 24h change | 1.77% |
| DEX volume (24h) | $2,235,068,600 |
| Stablecoin supply | $16,016,617,243.88 |
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