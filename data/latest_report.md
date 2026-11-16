# Solana Ecosystem Report
_Generated 2026-11-16T16:53:26+00:00_

## Anomalies

- **[WARNING]** Validator delinquency at 5.44% (>= 5% threshold).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 470,205,657 |
| Current epoch | 1,088 |
| Epoch progress | 43.9% |
| Avg TPS (recent) | 1,925.79 |
| Max TPS (recent) | 2,484.8 |
| Avg slot time | 214.93 ms |
| Cluster health | ok |

## Validator status

- Active validators: **661**
- Delinquent validators: **38**
- Delinquency rate: **5.44%**
- Total active stake: **429,145,034.28 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 16,936,855.42 | 3.947% | 0% |
| 2 | `CcaHc2L4…` | 16,432,361.16 | 3.829% | 7% |
| 3 | `3N7s9zXM…` | 12,486,687.02 | 2.91% | 0% |
| 4 | `8GbwASqd…` | 10,142,841.82 | 2.363% | 0% |
| 5 | `51JBzSTU…` | 9,787,747.51 | 2.281% | 10% |
| 6 | `CatzoSMU…` | 9,620,150.11 | 2.242% | 5% |
| 7 | `26pV97Ce…` | 9,212,349.98 | 2.147% | 7% |
| 8 | `9QU2QSxh…` | 7,959,108.43 | 1.855% | 7% |
| 9 | `DumiCKHV…` | 6,992,227.25 | 1.629% | 0% |
| 10 | `CvSb7wdQ…` | 6,709,565.78 | 1.563% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $71.08 |
| 24h price change | -0.18% |
| Market cap | $42,051,706,043.0301 |
| 24h volume | $2,916,256,992.9804425 |
| Solana TVL | $4,680,384,007 |
| TVL 24h change | 1.21% |
| DEX volume (24h) | $1,352,559,060.0900002 |
| Stablecoin supply | $14,370,873,336.66 |
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