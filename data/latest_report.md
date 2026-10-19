# Solana Ecosystem Report
_Generated 2026-10-19T06:41:22+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 458,737,116 |
| Current epoch | 1,061 |
| Epoch progress | 89.14% |
| Avg TPS (recent) | 4,605.13 |
| Max TPS (recent) | 5,722.67 |
| Avg slot time | 216.89 ms |
| Cluster health | ok |

## Validator status

- Active validators: **667**
- Delinquent validators: **13**
- Delinquency rate: **1.91%**
- Total active stake: **437,350,802.85 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,091,304.3 | 3.908% | 7% |
| 2 | `he1iusun…` | 15,762,758.43 | 3.604% | 0% |
| 3 | `3N7s9zXM…` | 12,523,730.06 | 2.864% | 0% |
| 4 | `8GbwASqd…` | 10,974,351.68 | 2.509% | 0% |
| 5 | `CatzoSMU…` | 9,718,483.62 | 2.222% | 5% |
| 6 | `51JBzSTU…` | 9,466,252.56 | 2.164% | 10% |
| 7 | `26pV97Ce…` | 9,251,163.73 | 2.115% | 7% |
| 8 | `9QU2QSxh…` | 7,774,268.16 | 1.778% | 7% |
| 9 | `CvSb7wdQ…` | 6,992,810.63 | 1.599% | 5% |
| 10 | `DumiCKHV…` | 6,730,669.7 | 1.539% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.75 |
| 24h price change | 2.04% |
| Market cap | $62,331,014,599.13645 |
| 24h volume | $2,544,016,593.1567287 |
| Solana TVL | $5,873,964,001 |
| TVL 24h change | -0.37% |
| DEX volume (24h) | $1,565,961,174.3799996 |
| Stablecoin supply | $15,843,173,397.31 |
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