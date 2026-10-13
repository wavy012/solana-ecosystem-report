# Solana Ecosystem Report
_Generated 2026-10-13T23:33:19+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 456,624,441 |
| Current epoch | 1,057 |
| Epoch progress | 0.09% |
| Avg TPS (recent) | 4,746.58 |
| Max TPS (recent) | 5,262.7 |
| Avg slot time | 217.97 ms |
| Cluster health | ok |

## Validator status

- Active validators: **672**
- Delinquent validators: **6**
- Delinquency rate: **0.88%**
- Total active stake: **438,120,960.04 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,793,645.7 | 4.061% | 7% |
| 2 | `he1iusun…` | 15,829,632.96 | 3.613% | 0% |
| 3 | `3N7s9zXM…` | 12,312,512.16 | 2.81% | 0% |
| 4 | `8GbwASqd…` | 11,142,533.04 | 2.543% | 0% |
| 5 | `CatzoSMU…` | 10,762,921.6 | 2.457% | 5% |
| 6 | `51JBzSTU…` | 9,406,692.86 | 2.147% | 10% |
| 7 | `26pV97Ce…` | 9,240,130.57 | 2.109% | 7% |
| 8 | `9QU2QSxh…` | 7,700,636.24 | 1.758% | 7% |
| 9 | `CvSb7wdQ…` | 6,906,650.98 | 1.576% | 5% |
| 10 | `3JD3jMmn…` | 6,638,837.36 | 1.515% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $106.72 |
| 24h price change | 0.74% |
| Market cap | $62,844,950,243.97215 |
| 24h volume | $3,802,689,836.182224 |
| Solana TVL | $6,034,398,523 |
| TVL 24h change | -3.03% |
| DEX volume (24h) | $2,231,842,381.02 |
| Stablecoin supply | $16,222,437,013.64 |
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