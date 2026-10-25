# Solana Ecosystem Report
_Generated 2026-10-25T17:44:22+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 461,346,563 |
| Current epoch | 1,067 |
| Epoch progress | 93.19% |
| Avg TPS (recent) | 1,665.97 |
| Max TPS (recent) | 2,044.53 |
| Avg slot time | 212.16 ms |
| Cluster health | ok |

## Validator status

- Active validators: **665**
- Delinquent validators: **25**
- Delinquency rate: **3.62%**
- Total active stake: **437,191,005.83 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,099,112.75 | 3.911% | 7% |
| 2 | `he1iusun…` | 16,646,121.33 | 3.808% | 0% |
| 3 | `3N7s9zXM…` | 12,588,035.11 | 2.879% | 0% |
| 4 | `8GbwASqd…` | 10,881,430.46 | 2.489% | 0% |
| 5 | `CatzoSMU…` | 9,721,917.56 | 2.224% | 5% |
| 6 | `51JBzSTU…` | 9,483,244.32 | 2.169% | 10% |
| 7 | `26pV97Ce…` | 9,216,836.58 | 2.108% | 7% |
| 8 | `9QU2QSxh…` | 7,785,035.62 | 1.781% | 7% |
| 9 | `CvSb7wdQ…` | 7,038,249.33 | 1.61% | 5% |
| 10 | `DumiCKHV…` | 7,006,652.89 | 1.603% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $101.84 |
| 24h price change | 1.63% |
| Market cap | $60,061,492,577.228714 |
| 24h volume | $1,444,323,706.9497418 |
| Solana TVL | $5,738,586,809 |
| TVL 24h change | -0.63% |
| DEX volume (24h) | $1,423,041,369.8 |
| Stablecoin supply | $15,937,418,669.58 |
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