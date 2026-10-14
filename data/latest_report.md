# Solana Ecosystem Report
_Generated 2026-10-14T22:00:05+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 456,996,621 |
| Current epoch | 1,057 |
| Epoch progress | 86.25% |
| Avg TPS (recent) | 5,268.16 |
| Max TPS (recent) | 6,042.87 |
| Avg slot time | 216.49 ms |
| Cluster health | ok |

## Validator status

- Active validators: **673**
- Delinquent validators: **5**
- Delinquency rate: **0.74%**
- Total active stake: **438,131,311.74 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,794,097.35 | 4.061% | 7% |
| 2 | `he1iusun…` | 15,830,159.7 | 3.613% | 0% |
| 3 | `3N7s9zXM…` | 12,313,026.65 | 2.81% | 0% |
| 4 | `8GbwASqd…` | 11,142,983.96 | 2.543% | 0% |
| 5 | `CatzoSMU…` | 10,763,192.27 | 2.457% | 5% |
| 6 | `51JBzSTU…` | 9,407,225.08 | 2.147% | 10% |
| 7 | `26pV97Ce…` | 9,240,433.63 | 2.109% | 7% |
| 8 | `9QU2QSxh…` | 7,700,930.91 | 1.758% | 7% |
| 9 | `CvSb7wdQ…` | 6,906,931.44 | 1.576% | 5% |
| 10 | `3JD3jMmn…` | 6,638,867.71 | 1.515% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.63 |
| 24h price change | -2.25% |
| Market cap | $61,649,378,033.191216 |
| 24h volume | $3,154,984,012.141824 |
| Solana TVL | $5,956,970,618 |
| TVL 24h change | -0.39% |
| DEX volume (24h) | $2,495,170,004.38 |
| Stablecoin supply | $16,325,854,364.52 |
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