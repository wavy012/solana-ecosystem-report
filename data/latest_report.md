# Solana Ecosystem Report
_Generated 2026-11-28T01:45:07+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 474,772,809 |
| Current epoch | 1,099 |
| Epoch progress | 1.11% |
| Avg TPS (recent) | 1,561.32 |
| Max TPS (recent) | 2,101.42 |
| Avg slot time | 213.51 ms |
| Cluster health | ok |

## Validator status

- Active validators: **654**
- Delinquent validators: **11**
- Delinquency rate: **1.65%**
- Total active stake: **423,553,544.37 SOL**
- Median commission: **5.0%**

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
| SOL price | $72.01 |
| 24h price change | 1.01% |
| Market cap | $42,668,653,087.83474 |
| 24h volume | $2,636,018,138.8339 |
| Solana TVL | $4,607,214,918 |
| TVL 24h change | -0.0% |
| DEX volume (24h) | $885,191,708.1200001 |
| Stablecoin supply | $13,427,937,216.51 |
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