# Solana Ecosystem Report
_Generated 2026-11-15T07:27:01+00:00_

## Anomalies

- **[WARNING]** TPS drop: 1122.42 vs rolling baseline 1833.44 (-38.8%).
- **[WARNING]** Validator delinquency at 5.43% (>= 5% threshold).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 469,645,366 |
| Current epoch | 1,087 |
| Epoch progress | 14.21% |
| Avg TPS (recent) | 1,122.42 |
| Max TPS (recent) | 1,329.48 |
| Avg slot time | 214.95 ms |
| Cluster health | ok |

## Validator status

- Active validators: **662**
- Delinquent validators: **38**
- Delinquency rate: **5.43%**
- Total active stake: **429,328,620.52 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 16,927,749.21 | 3.943% | 0% |
| 2 | `CcaHc2L4…` | 16,404,543.75 | 3.821% | 7% |
| 3 | `3N7s9zXM…` | 12,614,560.66 | 2.938% | 0% |
| 4 | `8GbwASqd…` | 10,141,932.01 | 2.362% | 0% |
| 5 | `51JBzSTU…` | 9,754,208.28 | 2.272% | 10% |
| 6 | `CatzoSMU…` | 9,640,656.01 | 2.246% | 5% |
| 7 | `26pV97Ce…` | 9,204,466.01 | 2.144% | 7% |
| 8 | `9QU2QSxh…` | 7,943,263.75 | 1.85% | 7% |
| 9 | `DumiCKHV…` | 6,991,231.92 | 1.628% | 0% |
| 10 | `CvSb7wdQ…` | 6,708,647.61 | 1.563% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.41 |
| 24h price change | -6.48% |
| Market cap | $41,646,190,161.6537 |
| 24h volume | $5,018,210,728.775713 |
| Solana TVL | $4,649,503,685 |
| TVL 24h change | -4.19% |
| DEX volume (24h) | $1,614,007,307.7 |
| Stablecoin supply | $14,254,111,001.039999 |
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