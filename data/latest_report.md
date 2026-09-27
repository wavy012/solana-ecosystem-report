# Solana Ecosystem Report
_Generated 2026-09-27T22:27:36+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 451,130,915 |
| Current epoch | 1,044 |
| Epoch progress | 28.45% |
| Avg TPS (recent) | 4,954.33 |
| Max TPS (recent) | 5,490.8 |
| Avg slot time | 269.86 ms |
| Cluster health | ok |

## Validator status

- Active validators: **675**
- Delinquent validators: **8**
- Delinquency rate: **1.17%**
- Total active stake: **440,549,806.65 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,867,778.86 | 4.056% | 7% |
| 2 | `he1iusun…` | 15,840,792.44 | 3.596% | 0% |
| 3 | `3N7s9zXM…` | 12,330,570.2 | 2.799% | 0% |
| 4 | `CatzoSMU…` | 11,215,731.52 | 2.546% | 5% |
| 5 | `8GbwASqd…` | 10,838,730.0 | 2.46% | 0% |
| 6 | `26pV97Ce…` | 9,238,854.02 | 2.097% | 7% |
| 7 | `51JBzSTU…` | 9,209,776.28 | 2.091% | 10% |
| 8 | `9QU2QSxh…` | 7,623,406.66 | 1.73% | 7% |
| 9 | `CvSb7wdQ…` | 7,094,526.07 | 1.61% | 5% |
| 10 | `DumiCKHV…` | 6,511,333.58 | 1.478% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $122.03 |
| 24h price change | 0.45% |
| Market cap | $71,724,963,924.23462 |
| 24h volume | $3,767,198,088.9356437 |
| Solana TVL | $6,708,092,448 |
| TVL 24h change | 1.09% |
| DEX volume (24h) | $2,155,234,120.21 |
| Stablecoin supply | $16,783,292,886.35 |
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