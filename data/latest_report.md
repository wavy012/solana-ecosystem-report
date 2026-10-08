# Solana Ecosystem Report
_Generated 2026-10-08T16:43:10+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 454,601,518 |
| Current epoch | 1,052 |
| Epoch progress | 31.83% |
| Avg TPS (recent) | 4,779.98 |
| Max TPS (recent) | 6,446.98 |
| Avg slot time | 270.51 ms |
| Cluster health | ok |

## Validator status

- Active validators: **671**
- Delinquent validators: **8**
- Delinquency rate: **1.18%**
- Total active stake: **439,005,452.64 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,819,093.93 | 4.059% | 7% |
| 2 | `he1iusun…` | 15,944,778.11 | 3.632% | 0% |
| 3 | `3N7s9zXM…` | 12,318,266.26 | 2.806% | 0% |
| 4 | `8GbwASqd…` | 11,224,868.23 | 2.557% | 0% |
| 5 | `CatzoSMU…` | 11,075,221.92 | 2.523% | 5% |
| 6 | `51JBzSTU…` | 9,267,423.2 | 2.111% | 10% |
| 7 | `26pV97Ce…` | 9,257,644.96 | 2.109% | 7% |
| 8 | `9QU2QSxh…` | 7,512,075.98 | 1.711% | 7% |
| 9 | `CvSb7wdQ…` | 6,812,500.09 | 1.552% | 5% |
| 10 | `3JD3jMmn…` | 6,691,194.46 | 1.524% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $108.75 |
| 24h price change | -6.83% |
| Market cap | $64,036,820,075.513405 |
| 24h volume | $3,962,895,950.288591 |
| Solana TVL | $6,333,948,634 |
| TVL 24h change | -4.44% |
| DEX volume (24h) | $2,205,685,057.8100004 |
| Stablecoin supply | $16,593,543,152.41 |
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