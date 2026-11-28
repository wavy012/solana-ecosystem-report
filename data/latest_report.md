# Solana Ecosystem Report
_Generated 2026-11-28T09:42:00+00:00_

## Anomalies

- **[WARNING]** TPS drop: 867.9 vs rolling baseline 1735.08 (-50.0%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 474,906,215 |
| Current epoch | 1,099 |
| Epoch progress | 32.0% |
| Avg TPS (recent) | 867.9 |
| Max TPS (recent) | 1,100.35 |
| Avg slot time | 214.38 ms |
| Cluster health | ok |

## Validator status

- Active validators: **655**
- Delinquent validators: **10**
- Delinquency rate: **1.5%**
- Total active stake: **423,553,544.37 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 16,820,638.61 | 3.971% | 0% |
| 2 | `CcaHc2L4…` | 15,937,963.55 | 3.763% | 7% |
| 3 | `3N7s9zXM…` | 12,430,258.65 | 2.935% | 0% |
| 4 | `8GbwASqd…` | 10,239,620.78 | 2.418% | 0% |
| 5 | `51JBzSTU…` | 9,920,125.48 | 2.342% | 10% |
| 6 | `CatzoSMU…` | 9,625,966.46 | 2.273% | 5% |
| 7 | `26pV97Ce…` | 9,299,547.51 | 2.196% | 7% |
| 8 | `9QU2QSxh…` | 8,045,358.35 | 1.899% | 7% |
| 9 | `DumiCKHV…` | 6,973,110.12 | 1.646% | 0% |
| 10 | `CvSb7wdQ…` | 6,346,579.32 | 1.498% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.87 |
| 24h price change | -3.78% |
| Market cap | $41,983,774,232.782364 |
| 24h volume | $2,231,372,549.791923 |
| Solana TVL | $4,586,185,789 |
| TVL 24h change | -0.89% |
| DEX volume (24h) | $942,999,811.38 |
| Stablecoin supply | $13,418,428,504.91 |
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