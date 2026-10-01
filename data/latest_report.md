# Solana Ecosystem Report
_Generated 2026-10-01T00:04:16+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 452,120,405 |
| Current epoch | 1,046 |
| Epoch progress | 57.49% |
| Avg TPS (recent) | 4,599.99 |
| Max TPS (recent) | 5,006.28 |
| Avg slot time | 268.58 ms |
| Cluster health | ok |

## Validator status

- Active validators: **672**
- Delinquent validators: **11**
- Delinquency rate: **1.61%**
- Total active stake: **440,549,644.99 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,227,375.87 | 3.91% | 7% |
| 2 | `he1iusun…` | 15,893,944.57 | 3.608% | 0% |
| 3 | `3N7s9zXM…` | 12,330,668.09 | 2.799% | 0% |
| 4 | `8GbwASqd…` | 11,384,141.14 | 2.584% | 0% |
| 5 | `CatzoSMU…` | 11,206,135.3 | 2.544% | 5% |
| 6 | `26pV97Ce…` | 9,257,721.06 | 2.101% | 7% |
| 7 | `51JBzSTU…` | 9,232,740.3 | 2.096% | 10% |
| 8 | `9QU2QSxh…` | 7,652,674.7 | 1.737% | 7% |
| 9 | `CvSb7wdQ…` | 7,092,577.15 | 1.61% | 5% |
| 10 | `DumiCKHV…` | 6,513,561.77 | 1.479% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $117.96 |
| 24h price change | -0.99% |
| Market cap | $69,370,867,575.14247 |
| 24h volume | $4,261,991,974.3300047 |
| Solana TVL | $6,525,112,380 |
| TVL 24h change | 1.06% |
| DEX volume (24h) | $2,534,187,471.8400006 |
| Stablecoin supply | $16,464,350,939.490002 |
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