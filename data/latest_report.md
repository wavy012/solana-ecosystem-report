# Solana Ecosystem Report
_Generated 2026-10-02T20:02:28+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 452,711,934 |
| Current epoch | 1,047 |
| Epoch progress | 94.42% |
| Avg TPS (recent) | 5,383.69 |
| Max TPS (recent) | 5,741.68 |
| Avg slot time | 268.48 ms |
| Cluster health | ok |

## Validator status

- Active validators: **672**
- Delinquent validators: **12**
- Delinquency rate: **1.75%**
- Total active stake: **440,810,473.09 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,839,408.08 | 4.047% | 7% |
| 2 | `he1iusun…` | 15,905,145.21 | 3.608% | 0% |
| 3 | `3N7s9zXM…` | 12,328,202.76 | 2.797% | 0% |
| 4 | `8GbwASqd…` | 11,357,265.11 | 2.576% | 0% |
| 5 | `CatzoSMU…` | 11,209,120.94 | 2.543% | 5% |
| 6 | `26pV97Ce…` | 9,267,703.98 | 2.102% | 7% |
| 7 | `51JBzSTU…` | 9,246,451.05 | 2.098% | 10% |
| 8 | `9QU2QSxh…` | 7,601,711.15 | 1.724% | 7% |
| 9 | `CvSb7wdQ…` | 7,063,975.16 | 1.602% | 5% |
| 10 | `3JD3jMmn…` | 6,682,304.84 | 1.516% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $117.99 |
| 24h price change | -0.34% |
| Market cap | $69,381,484,148.64938 |
| 24h volume | $4,725,930,786.570888 |
| Solana TVL | $6,655,125,733 |
| TVL 24h change | 2.27% |
| DEX volume (24h) | $2,488,460,102.88 |
| Stablecoin supply | $16,562,389,752.980001 |
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