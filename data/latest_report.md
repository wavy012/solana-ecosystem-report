# Solana Ecosystem Report
_Generated 2026-11-24T21:27:00+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 473,494,633 |
| Current epoch | 1,096 |
| Epoch progress | 5.24% |
| Avg TPS (recent) | 2,027.01 |
| Max TPS (recent) | 3,131.72 |
| Avg slot time | 214.47 ms |
| Cluster health | ok |

## Validator status

- Active validators: **660**
- Delinquent validators: **27**
- Delinquency rate: **3.93%**
- Total active stake: **424,794,569.44 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 17,003,541.98 | 4.003% | 0% |
| 2 | `CcaHc2L4…` | 15,962,658.49 | 3.758% | 7% |
| 3 | `3N7s9zXM…` | 12,418,811.68 | 2.923% | 0% |
| 4 | `8GbwASqd…` | 10,242,949.23 | 2.411% | 0% |
| 5 | `51JBzSTU…` | 9,885,208.79 | 2.327% | 10% |
| 6 | `CatzoSMU…` | 9,615,268.5 | 2.264% | 5% |
| 7 | `26pV97Ce…` | 9,283,846.82 | 2.185% | 7% |
| 8 | `9QU2QSxh…` | 8,016,084.55 | 1.887% | 7% |
| 9 | `DumiCKHV…` | 6,968,432.36 | 1.64% | 0% |
| 10 | `CvSb7wdQ…` | 6,779,378.02 | 1.596% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $69.38 |
| 24h price change | -4.26% |
| Market cap | $41,080,245,079.280136 |
| 24h volume | $2,580,575,503.525487 |
| Solana TVL | $4,511,885,953 |
| TVL 24h change | 0.0% |
| DEX volume (24h) | $1,805,966,413.26 |
| Stablecoin supply | $13,918,367,981.949999 |
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