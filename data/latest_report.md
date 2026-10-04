# Solana Ecosystem Report
_Generated 2026-10-04T23:24:08+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 453,403,107 |
| Current epoch | 1,049 |
| Epoch progress | 54.42% |
| Avg TPS (recent) | 4,799.55 |
| Max TPS (recent) | 5,211.65 |
| Avg slot time | 268.28 ms |
| Cluster health | ok |

## Validator status

- Active validators: **671**
- Delinquent validators: **15**
- Delinquency rate: **2.19%**
- Total active stake: **441,848,823.05 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,935,561.86 | 4.059% | 7% |
| 2 | `he1iusun…` | 15,927,648.99 | 3.605% | 0% |
| 3 | `3N7s9zXM…` | 12,346,574.39 | 2.794% | 0% |
| 4 | `8GbwASqd…` | 11,305,934.57 | 2.559% | 0% |
| 5 | `CatzoSMU…` | 11,136,537.41 | 2.52% | 5% |
| 6 | `26pV97Ce…` | 9,254,654.76 | 2.095% | 7% |
| 7 | `51JBzSTU…` | 9,241,331.23 | 2.092% | 10% |
| 8 | `9QU2QSxh…` | 7,616,096.57 | 1.724% | 7% |
| 9 | `CvSb7wdQ…` | 7,061,519.22 | 1.598% | 5% |
| 10 | `3JD3jMmn…` | 6,686,110.61 | 1.513% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $121.89 |
| 24h price change | 1.77% |
| Market cap | $71,709,219,182.22427 |
| 24h volume | $2,072,103,496.6903493 |
| Solana TVL | $6,722,257,989 |
| TVL 24h change | 1.48% |
| DEX volume (24h) | $1,553,984,451.1100001 |
| Stablecoin supply | $16,860,942,429.14 |
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