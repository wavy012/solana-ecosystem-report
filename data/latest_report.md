# Solana Ecosystem Report
_Generated 2026-09-15T17:52:57+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 447,311,548 |
| Current epoch | 1,035 |
| Epoch progress | 44.33% |
| Avg TPS (recent) | 4,475.87 |
| Max TPS (recent) | 5,212.93 |
| Avg slot time | 316.6 ms |
| Cluster health | ok |

## Validator status

- Active validators: **679**
- Delinquent validators: **10**
- Delinquency rate: **1.45%**
- Total active stake: **439,248,639.21 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,757,711.87 | 4.043% | 7% |
| 2 | `he1iusun…` | 16,373,376.88 | 3.728% | 0% |
| 3 | `3N7s9zXM…` | 12,492,604.95 | 2.844% | 0% |
| 4 | `CatzoSMU…` | 11,369,566.14 | 2.588% | 5% |
| 5 | `8GbwASqd…` | 9,669,319.45 | 2.201% | 0% |
| 6 | `26pV97Ce…` | 9,256,224.98 | 2.107% | 7% |
| 7 | `51JBzSTU…` | 9,035,102.59 | 2.057% | 10% |
| 8 | `9QU2QSxh…` | 7,372,354.85 | 1.678% | 7% |
| 9 | `CvSb7wdQ…` | 6,944,775.01 | 1.581% | 5% |
| 10 | `DumiCKHV…` | 6,553,625.65 | 1.492% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $100.48 |
| 24h price change | -2.43% |
| Market cap | $58,974,218,154.2275 |
| 24h volume | $3,373,828,314.960949 |
| Solana TVL | $5,780,349,506 |
| TVL 24h change | -0.95% |
| DEX volume (24h) | $2,530,223,236.85 |
| Stablecoin supply | $16,368,181,115.99 |
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