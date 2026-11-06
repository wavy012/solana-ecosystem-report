# Solana Ecosystem Report
_Generated 2026-11-06T18:11:06+00:00_

## Anomalies

- **[WARNING]** Validator delinquency at 5.46% (>= 5% threshold).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 466,205,287 |
| Current epoch | 1,079 |
| Epoch progress | 17.89% |
| Avg TPS (recent) | 2,217.05 |
| Max TPS (recent) | 3,572.15 |
| Avg slot time | 214.54 ms |
| Cluster health | ok |

## Validator status

- Active validators: **658**
- Delinquent validators: **38**
- Delinquency rate: **5.46%**
- Total active stake: **434,917,723.21 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,039,555.63 | 3.918% | 7% |
| 2 | `he1iusun…` | 16,722,208.51 | 3.845% | 0% |
| 3 | `3N7s9zXM…` | 13,017,562.49 | 2.993% | 0% |
| 4 | `8GbwASqd…` | 10,436,419.69 | 2.4% | 0% |
| 5 | `CatzoSMU…` | 9,531,945.75 | 2.192% | 5% |
| 6 | `51JBzSTU…` | 9,519,641.83 | 2.189% | 10% |
| 7 | `26pV97Ce…` | 9,240,518.58 | 2.125% | 7% |
| 8 | `9QU2QSxh…` | 7,741,932.94 | 1.78% | 7% |
| 9 | `CvSb7wdQ…` | 6,982,918.21 | 1.606% | 5% |
| 10 | `DumiCKHV…` | 6,971,613.57 | 1.603% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $90.03 |
| 24h price change | 1.23% |
| Market cap | $53,156,785,325.62102 |
| 24h volume | $2,829,660,426.957256 |
| Solana TVL | $5,284,877,008 |
| TVL 24h change | -4.5% |
| DEX volume (24h) | $2,198,364,299.2 |
| Stablecoin supply | $15,180,532,675.24 |
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