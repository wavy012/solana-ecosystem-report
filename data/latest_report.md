# Solana Ecosystem Report
_Generated 2026-11-05T08:58:06+00:00_

## Anomalies

- **[WARNING]** TPS drop: 1184.05 vs rolling baseline 1746.82 (-32.2%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 465,646,213 |
| Current epoch | 1,077 |
| Epoch progress | 88.48% |
| Avg TPS (recent) | 1,184.05 |
| Max TPS (recent) | 1,406.95 |
| Avg slot time | 212.22 ms |
| Cluster health | ok |

## Validator status

- Active validators: **662**
- Delinquent validators: **31**
- Delinquency rate: **4.47%**
- Total active stake: **433,017,789.22 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,036,630.97 | 3.934% | 7% |
| 2 | `he1iusun…` | 16,710,688.82 | 3.859% | 0% |
| 3 | `3N7s9zXM…` | 13,012,272.19 | 3.005% | 0% |
| 4 | `8GbwASqd…` | 10,433,406.27 | 2.409% | 0% |
| 5 | `CatzoSMU…` | 9,524,736.37 | 2.2% | 5% |
| 6 | `51JBzSTU…` | 9,439,186.26 | 2.18% | 10% |
| 7 | `26pV97Ce…` | 9,217,929.68 | 2.129% | 7% |
| 8 | `9QU2QSxh…` | 7,826,696.89 | 1.807% | 7% |
| 9 | `DumiCKHV…` | 6,981,456.97 | 1.612% | 0% |
| 10 | `CvSb7wdQ…` | 6,980,105.04 | 1.612% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $96.61 |
| 24h price change | 3.73% |
| Market cap | $57,024,952,747.079124 |
| 24h volume | $4,159,786,154.4881234 |
| Solana TVL | $5,538,024,255 |
| TVL 24h change | 2.89% |
| DEX volume (24h) | $2,222,398,076.94 |
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