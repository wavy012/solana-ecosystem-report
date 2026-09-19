# Solana Ecosystem Report
_Generated 2026-09-19T19:54:50+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 448,507,951 |
| Current epoch | 1,038 |
| Epoch progress | 21.28% |
| Avg TPS (recent) | 4,519.68 |
| Max TPS (recent) | 5,243.52 |
| Avg slot time | 267.31 ms |
| Cluster health | ok |

## Validator status

- Active validators: **677**
- Delinquent validators: **13**
- Delinquency rate: **1.88%**
- Total active stake: **440,227,371.13 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,849,776.18 | 4.055% | 7% |
| 2 | `he1iusun…` | 15,819,246.86 | 3.593% | 0% |
| 3 | `3N7s9zXM…` | 12,500,805.32 | 2.84% | 0% |
| 4 | `CatzoSMU…` | 11,362,749.11 | 2.581% | 5% |
| 5 | `8GbwASqd…` | 9,786,807.17 | 2.223% | 0% |
| 6 | `26pV97Ce…` | 9,252,842.8 | 2.102% | 7% |
| 7 | `51JBzSTU…` | 9,116,740.01 | 2.071% | 10% |
| 8 | `9QU2QSxh…` | 7,434,775.77 | 1.689% | 7% |
| 9 | `CvSb7wdQ…` | 7,086,870.7 | 1.61% | 5% |
| 10 | `HZKopZYv…` | 6,627,951.1 | 1.506% | 100% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $111.26 |
| 24h price change | -2.37% |
| Market cap | $65,348,159,309.93939 |
| 24h volume | $3,273,294,858.608001 |
| Solana TVL | $6,243,234,676 |
| TVL 24h change | 5.87% |
| DEX volume (24h) | $3,536,797,881.43 |
| Stablecoin supply | $15,855,850,707.36 |
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