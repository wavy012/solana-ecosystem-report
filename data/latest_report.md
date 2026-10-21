# Solana Ecosystem Report
_Generated 2026-10-21T20:15:58+00:00_

## Anomalies

- **[WARNING]** TPS drop: 2314.43 vs rolling baseline 4882.6 (-52.6%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 459,760,708 |
| Current epoch | 1,064 |
| Epoch progress | 26.09% |
| Avg TPS (recent) | 2,314.43 |
| Max TPS (recent) | 2,981.75 |
| Avg slot time | 212.84 ms |
| Cluster health | ok |

## Validator status

- Active validators: **668**
- Delinquent validators: **9**
- Delinquency rate: **1.33%**
- Total active stake: **438,868,046.05 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,130,984.07 | 3.903% | 7% |
| 2 | `he1iusun…` | 15,955,653.26 | 3.636% | 0% |
| 3 | `3N7s9zXM…` | 12,545,893.8 | 2.859% | 0% |
| 4 | `8GbwASqd…` | 10,933,490.63 | 2.491% | 0% |
| 5 | `CatzoSMU…` | 9,728,193.28 | 2.217% | 5% |
| 6 | `51JBzSTU…` | 9,480,473.67 | 2.16% | 10% |
| 7 | `26pV97Ce…` | 9,252,296.09 | 2.108% | 7% |
| 8 | `9QU2QSxh…` | 7,808,121.6 | 1.779% | 7% |
| 9 | `CvSb7wdQ…` | 7,035,084.97 | 1.603% | 5% |
| 10 | `DumiCKHV…` | 7,001,556.65 | 1.595% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $108.22 |
| 24h price change | 2.1% |
| Market cap | $63,805,949,701.9196 |
| 24h volume | $2,486,986,679.6489563 |
| Solana TVL | $6,028,642,603 |
| TVL 24h change | 3.11% |
| DEX volume (24h) | $2,437,800,216.24 |
| Stablecoin supply | $16,016,617,243.88 |
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