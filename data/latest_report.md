# Solana Ecosystem Report
_Generated 2026-09-19T11:17:42+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 448,391,697 |
| Current epoch | 1,037 |
| Epoch progress | 94.37% |
| Avg TPS (recent) | 3,828.55 |
| Max TPS (recent) | 4,153.63 |
| Avg slot time | 264.99 ms |
| Cluster health | ok |

## Validator status

- Active validators: **677**
- Delinquent validators: **11**
- Delinquency rate: **1.6%**
- Total active stake: **439,612,407.68 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,815,472.4 | 4.053% | 7% |
| 2 | `he1iusun…` | 15,816,148.04 | 3.598% | 0% |
| 3 | `3N7s9zXM…` | 12,510,307.73 | 2.846% | 0% |
| 4 | `CatzoSMU…` | 11,398,201.71 | 2.593% | 5% |
| 5 | `8GbwASqd…` | 9,784,908.12 | 2.226% | 0% |
| 6 | `26pV97Ce…` | 9,254,525.6 | 2.105% | 7% |
| 7 | `51JBzSTU…` | 9,077,527.04 | 2.065% | 10% |
| 8 | `9QU2QSxh…` | 7,397,868.72 | 1.683% | 7% |
| 9 | `CvSb7wdQ…` | 7,085,577.98 | 1.612% | 5% |
| 10 | `DumiCKHV…` | 6,557,939.5 | 1.492% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $111.72 |
| 24h price change | 5.86% |
| Market cap | $65,614,918,165.161125 |
| 24h volume | $5,408,102,079.205433 |
| Solana TVL | $6,248,192,665 |
| TVL 24h change | 5.95% |
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