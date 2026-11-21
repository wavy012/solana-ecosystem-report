# Solana Ecosystem Report
_Generated 2026-11-21T09:05:45+00:00_

## Anomalies

- **[WARNING]** TPS drop: 1159.17 vs rolling baseline 1786.65 (-35.1%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 472,082,381 |
| Current epoch | 1,092 |
| Epoch progress | 78.33% |
| Avg TPS (recent) | 1,159.17 |
| Max TPS (recent) | 1,593.03 |
| Avg slot time | 214.91 ms |
| Cluster health | ok |

## Validator status

- Active validators: **661**
- Delinquent validators: **24**
- Delinquency rate: **3.5%**
- Total active stake: **428,985,796.8 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 17,041,637.89 | 3.973% | 0% |
| 2 | `CcaHc2L4…` | 16,354,101.2 | 3.812% | 7% |
| 3 | `3N7s9zXM…` | 12,422,891.16 | 2.896% | 0% |
| 4 | `8GbwASqd…` | 10,309,120.92 | 2.403% | 0% |
| 5 | `51JBzSTU…` | 9,779,397.3 | 2.28% | 10% |
| 6 | `CatzoSMU…` | 9,564,402.59 | 2.23% | 5% |
| 7 | `26pV97Ce…` | 9,231,683.14 | 2.152% | 7% |
| 8 | `9QU2QSxh…` | 7,986,182.36 | 1.862% | 7% |
| 9 | `DumiCKHV…` | 6,985,765.18 | 1.628% | 0% |
| 10 | `CvSb7wdQ…` | 6,773,182.11 | 1.579% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $67.28 |
| 24h price change | -7.04% |
| Market cap | $39,828,630,674.205376 |
| 24h volume | $4,678,766,437.088335 |
| Solana TVL | $4,488,478,379 |
| TVL 24h change | -4.72% |
| DEX volume (24h) | $1,836,080,739.35 |
| Stablecoin supply | $13,288,934,081.24 |
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