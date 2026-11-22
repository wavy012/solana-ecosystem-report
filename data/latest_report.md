# Solana Ecosystem Report
_Generated 2026-11-22T17:33:14+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 472,625,947 |
| Current epoch | 1,094 |
| Epoch progress | 4.15% |
| Avg TPS (recent) | 1,815.65 |
| Max TPS (recent) | 2,275.72 |
| Avg slot time | 214.31 ms |
| Cluster health | ok |

## Validator status

- Active validators: **661**
- Delinquent validators: **24**
- Delinquency rate: **3.5%**
- Total active stake: **425,691,542.02 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 16,918,439.8 | 3.974% | 0% |
| 2 | `CcaHc2L4…` | 16,346,958.71 | 3.84% | 7% |
| 3 | `3N7s9zXM…` | 12,401,889.01 | 2.913% | 0% |
| 4 | `8GbwASqd…` | 10,243,004.56 | 2.406% | 0% |
| 5 | `51JBzSTU…` | 9,842,252.9 | 2.312% | 10% |
| 6 | `CatzoSMU…` | 9,612,895.64 | 2.258% | 5% |
| 7 | `26pV97Ce…` | 9,269,554.51 | 2.178% | 7% |
| 8 | `9QU2QSxh…` | 7,998,894.55 | 1.879% | 7% |
| 9 | `DumiCKHV…` | 6,987,495.14 | 1.641% | 0% |
| 10 | `CvSb7wdQ…` | 6,775,083.09 | 1.592% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.34 |
| 24h price change | -0.42% |
| Market cap | $41,646,975,183.37765 |
| 24h volume | $1,849,799,715.6010387 |
| Solana TVL | $4,608,709,340 |
| TVL 24h change | 1.3% |
| DEX volume (24h) | $1,345,931,988.87 |
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