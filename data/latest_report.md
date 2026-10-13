# Solana Ecosystem Report
_Generated 2026-10-13T12:50:21+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 456,448,197 |
| Current epoch | 1,056 |
| Epoch progress | 59.3% |
| Avg TPS (recent) | 5,090.87 |
| Max TPS (recent) | 5,679.87 |
| Avg slot time | 219.62 ms |
| Cluster health | ok |

## Validator status

- Active validators: **673**
- Delinquent validators: **7**
- Delinquency rate: **1.03%**
- Total active stake: **438,790,522.18 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,789,243.07 | 4.054% | 7% |
| 2 | `he1iusun…` | 15,958,932.38 | 3.637% | 0% |
| 3 | `3N7s9zXM…` | 12,305,752.01 | 2.804% | 0% |
| 4 | `8GbwASqd…` | 11,149,128.55 | 2.541% | 0% |
| 5 | `CatzoSMU…` | 10,758,267.52 | 2.452% | 5% |
| 6 | `51JBzSTU…` | 9,401,788.21 | 2.143% | 10% |
| 7 | `26pV97Ce…` | 9,237,163.3 | 2.105% | 7% |
| 8 | `9QU2QSxh…` | 7,681,229.04 | 1.751% | 7% |
| 9 | `CvSb7wdQ…` | 6,812,455.99 | 1.553% | 5% |
| 10 | `3JD3jMmn…` | 6,638,148.37 | 1.513% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $106.43 |
| 24h price change | -3.64% |
| Market cap | $62,706,797,862.80652 |
| 24h volume | $4,207,293,945.882638 |
| Solana TVL | $6,042,267,645 |
| TVL 24h change | -2.91% |
| DEX volume (24h) | $2,231,841,478.02 |
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