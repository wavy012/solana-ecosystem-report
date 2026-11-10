# Solana Ecosystem Report
_Generated 2026-11-10T01:41:47+00:00_

## Anomalies

- **[WARNING]** Validator delinquency at 5.87% (>= 5% threshold).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 467,539,281 |
| Current epoch | 1,082 |
| Epoch progress | 26.69% |
| Avg TPS (recent) | 1,529.75 |
| Max TPS (recent) | 2,348.13 |
| Avg slot time | 214.29 ms |
| Cluster health | ok |

## Validator status

- Active validators: **657**
- Delinquent validators: **41**
- Delinquency rate: **5.87%**
- Total active stake: **434,984,472.35 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 16,898,208.43 | 3.885% | 7% |
| 2 | `he1iusun…` | 16,746,254.08 | 3.85% | 0% |
| 3 | `3N7s9zXM…` | 13,034,244.04 | 2.996% | 0% |
| 4 | `8GbwASqd…` | 10,280,950.21 | 2.364% | 0% |
| 5 | `51JBzSTU…` | 9,598,548.58 | 2.207% | 10% |
| 6 | `CatzoSMU…` | 9,553,850.87 | 2.196% | 5% |
| 7 | `26pV97Ce…` | 9,233,158.91 | 2.123% | 7% |
| 8 | `9QU2QSxh…` | 7,813,315.88 | 1.796% | 7% |
| 9 | `DumiCKHV…` | 6,987,971.49 | 1.606% | 0% |
| 10 | `CvSb7wdQ…` | 6,712,230.59 | 1.543% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $86.41 |
| 24h price change | -1.34% |
| Market cap | $51,063,233,315.112015 |
| 24h volume | $2,367,253,067.871081 |
| Solana TVL | $5,063,413,830 |
| TVL 24h change | -0.0% |
| DEX volume (24h) | $1,191,614,437.6399999 |
| Stablecoin supply | $14,863,405,519.810001 |
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