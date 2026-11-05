# Solana Ecosystem Report
_Generated 2026-11-05T17:10:49+00:00_

## Anomalies

- **[WARNING]** TPS spike: 2623.62 vs rolling baseline 1743.89 (50.4%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 465,784,728 |
| Current epoch | 1,078 |
| Epoch progress | 20.54% |
| Avg TPS (recent) | 2,623.62 |
| Max TPS (recent) | 3,205.82 |
| Avg slot time | 213.88 ms |
| Cluster health | ok |

## Validator status

- Active validators: **663**
- Delinquent validators: **31**
- Delinquency rate: **4.47%**
- Total active stake: **430,872,481.82 SOL**
- Median commission: **5%**

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
| SOL price | $89.94 |
| 24h price change | -6.55% |
| Market cap | $53,082,103,657.76525 |
| 24h volume | $4,418,849,644.934836 |
| Solana TVL | $5,384,218,338 |
| TVL 24h change | 0.03% |
| DEX volume (24h) | $2,385,538,829.94 |
| Stablecoin supply | $15,331,066,359.279999 |
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