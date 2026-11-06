# Solana Ecosystem Report
_Generated 2026-11-06T11:16:36+00:00_

## Anomalies

- **[WARNING]** TPS drop: 1176.69 vs rolling baseline 1807.12 (-34.9%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 466,089,348 |
| Current epoch | 1,078 |
| Epoch progress | 91.05% |
| Avg TPS (recent) | 1,176.69 |
| Max TPS (recent) | 1,401.75 |
| Avg slot time | 213.4 ms |
| Cluster health | ok |

## Validator status

- Active validators: **662**
- Delinquent validators: **32**
- Delinquency rate: **4.61%**
- Total active stake: **430,872,481.82 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,063,613.38 | 3.96% | 7% |
| 2 | `he1iusun…` | 16,736,545.63 | 3.884% | 0% |
| 3 | `3N7s9zXM…` | 13,020,023.68 | 3.022% | 0% |
| 4 | `8GbwASqd…` | 10,434,901.29 | 2.422% | 0% |
| 5 | `CatzoSMU…` | 9,530,733.43 | 2.212% | 5% |
| 6 | `51JBzSTU…` | 9,459,109.34 | 2.195% | 10% |
| 7 | `26pV97Ce…` | 9,222,691.68 | 2.14% | 7% |
| 8 | `9QU2QSxh…` | 7,860,096.14 | 1.824% | 7% |
| 9 | `DumiCKHV…` | 6,991,476.9 | 1.623% | 0% |
| 10 | `3JD3jMmn…` | 6,293,075.92 | 1.461% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $89.92 |
| 24h price change | -6.86% |
| Market cap | $53,090,208,852.67941 |
| 24h volume | $3,727,938,996.9488964 |
| Solana TVL | $5,277,619,611 |
| TVL 24h change | -4.57% |
| DEX volume (24h) | $2,182,575,633.2 |
| Stablecoin supply | $15,180,532,675.24 |
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