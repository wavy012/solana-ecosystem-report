# Solana Ecosystem Report
_Generated 2026-10-12T17:14:44+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 456,125,057 |
| Current epoch | 1,055 |
| Epoch progress | 84.5% |
| Avg TPS (recent) | 5,624.23 |
| Max TPS (recent) | 6,371.8 |
| Avg slot time | 220.1 ms |
| Cluster health | ok |

## Validator status

- Active validators: **673**
- Delinquent validators: **8**
- Delinquency rate: **1.17%**
- Total active stake: **438,762,140.06 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,781,884.57 | 4.053% | 7% |
| 2 | `he1iusun…` | 15,956,121.95 | 3.637% | 0% |
| 3 | `3N7s9zXM…` | 12,320,022.82 | 2.808% | 0% |
| 4 | `8GbwASqd…` | 11,147,729.04 | 2.541% | 0% |
| 5 | `CatzoSMU…` | 10,755,462.85 | 2.451% | 5% |
| 6 | `51JBzSTU…` | 9,332,199.02 | 2.127% | 10% |
| 7 | `26pV97Ce…` | 9,248,709.85 | 2.108% | 7% |
| 8 | `9QU2QSxh…` | 7,607,284.2 | 1.734% | 7% |
| 9 | `CvSb7wdQ…` | 6,811,093.73 | 1.552% | 5% |
| 10 | `3JD3jMmn…` | 6,422,658.38 | 1.464% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $107.93 |
| 24h price change | -3.49% |
| Market cap | $63,570,109,776.01165 |
| 24h volume | $2,770,230,240.0480514 |
| Solana TVL | $6,168,803,236 |
| TVL 24h change | -0.64% |
| DEX volume (24h) | $1,277,023,682.3100002 |
| Stablecoin supply | $16,341,834,370.81 |
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