# Solana Ecosystem Report
_Generated 2026-11-22T01:58:43+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 472,365,108 |
| Current epoch | 1,093 |
| Epoch progress | 43.78% |
| Avg TPS (recent) | 1,634.87 |
| Max TPS (recent) | 2,090.37 |
| Avg slot time | 214.75 ms |
| Cluster health | ok |

## Validator status

- Active validators: **661**
- Delinquent validators: **24**
- Delinquency rate: **3.5%**
- Total active stake: **428,316,392.11 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 17,043,671.14 | 3.979% | 0% |
| 2 | `CcaHc2L4…` | 16,329,817.4 | 3.813% | 7% |
| 3 | `3N7s9zXM…` | 12,412,620.37 | 2.898% | 0% |
| 4 | `8GbwASqd…` | 10,241,723.67 | 2.391% | 0% |
| 5 | `51JBzSTU…` | 9,826,792.86 | 2.294% | 10% |
| 6 | `CatzoSMU…` | 9,616,960.74 | 2.245% | 5% |
| 7 | `26pV97Ce…` | 9,237,166.0 | 2.157% | 7% |
| 8 | `9QU2QSxh…` | 7,985,736.68 | 1.864% | 7% |
| 9 | `DumiCKHV…` | 6,985,062.5 | 1.631% | 0% |
| 10 | `CvSb7wdQ…` | 6,774,153.83 | 1.582% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.26 |
| 24h price change | 2.38% |
| Market cap | $41,585,873,921.50117 |
| 24h volume | $3,597,790,156.6338863 |
| Solana TVL | $4,599,027,633 |
| TVL 24h change | 0.0% |
| DEX volume (24h) | $1,560,565,539.87 |
| Stablecoin supply | $13,395,720,227.5 |
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