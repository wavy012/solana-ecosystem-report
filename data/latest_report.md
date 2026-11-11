# Solana Ecosystem Report
_Generated 2026-11-11T02:04:22+00:00_

## Anomalies

- **[WARNING]** Validator delinquency at 5.87% (>= 5% threshold).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 467,948,847 |
| Current epoch | 1,083 |
| Epoch progress | 21.49% |
| Avg TPS (recent) | 1,826.43 |
| Max TPS (recent) | 2,429.03 |
| Avg slot time | 214.63 ms |
| Cluster health | ok |

## Validator status

- Active validators: **658**
- Delinquent validators: **41**
- Delinquency rate: **5.87%**
- Total active stake: **433,423,963.79 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 16,764,484.66 | 3.868% | 0% |
| 2 | `CcaHc2L4…` | 16,564,684.86 | 3.822% | 7% |
| 3 | `3N7s9zXM…` | 13,031,624.88 | 3.007% | 0% |
| 4 | `8GbwASqd…` | 10,117,254.31 | 2.334% | 0% |
| 5 | `51JBzSTU…` | 9,644,050.74 | 2.225% | 10% |
| 6 | `CatzoSMU…` | 9,571,015.38 | 2.208% | 5% |
| 7 | `26pV97Ce…` | 9,231,999.47 | 2.13% | 7% |
| 8 | `9QU2QSxh…` | 7,814,330.21 | 1.803% | 7% |
| 9 | `DumiCKHV…` | 6,987,247.64 | 1.612% | 0% |
| 10 | `CvSb7wdQ…` | 6,729,844.65 | 1.553% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $83.21 |
| 24h price change | -3.4% |
| Market cap | $49,207,367,899.829094 |
| 24h volume | $2,923,789,308.918921 |
| Solana TVL | $5,033,796,098 |
| TVL 24h change | 0.19% |
| DEX volume (24h) | $1,336,389,510.3400002 |
| Stablecoin supply | $14,813,594,699.13 |
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