# Solana Ecosystem Report
_Generated 2026-11-19T05:32:11+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 471,219,751 |
| Current epoch | 1,090 |
| Epoch progress | 78.65% |
| Avg TPS (recent) | 1,673.47 |
| Max TPS (recent) | 2,480.18 |
| Avg slot time | 214.72 ms |
| Cluster health | ok |

## Validator status

- Active validators: **660**
- Delinquent validators: **25**
- Delinquency rate: **3.65%**
- Total active stake: **426,746,615.63 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 17,030,758.55 | 3.991% | 0% |
| 2 | `CcaHc2L4…` | 16,476,078.06 | 3.861% | 7% |
| 3 | `3N7s9zXM…` | 12,423,469.92 | 2.911% | 0% |
| 4 | `8GbwASqd…` | 10,297,722.42 | 2.413% | 0% |
| 5 | `51JBzSTU…` | 9,815,429.72 | 2.3% | 10% |
| 6 | `CatzoSMU…` | 9,574,561.83 | 2.244% | 5% |
| 7 | `26pV97Ce…` | 9,222,715.31 | 2.161% | 7% |
| 8 | `9QU2QSxh…` | 7,973,219.71 | 1.868% | 7% |
| 9 | `DumiCKHV…` | 6,996,719.76 | 1.64% | 0% |
| 10 | `CvSb7wdQ…` | 6,771,471.63 | 1.587% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $74.49 |
| 24h price change | -1.29% |
| Market cap | $44,084,680,043.17387 |
| 24h volume | $2,138,537,044.1674588 |
| Solana TVL | $4,729,041,943 |
| TVL 24h change | -1.41% |
| DEX volume (24h) | $1,701,658,023.3100002 |
| Stablecoin supply | $13,084,756,273.61 |
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