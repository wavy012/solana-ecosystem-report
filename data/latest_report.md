# Solana Ecosystem Report
_Generated 2026-09-22T23:25:38+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 449,526,140 |
| Current epoch | 1,040 |
| Epoch progress | 56.97% |
| Avg TPS (recent) | 4,566.54 |
| Max TPS (recent) | 5,193.72 |
| Avg slot time | 267.37 ms |
| Cluster health | ok |

## Validator status

- Active validators: **677**
- Delinquent validators: **12**
- Delinquency rate: **1.74%**
- Total active stake: **439,861,749.26 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,826,722.02 | 4.053% | 7% |
| 2 | `he1iusun…` | 15,840,698.17 | 3.601% | 0% |
| 3 | `3N7s9zXM…` | 12,354,353.49 | 2.809% | 0% |
| 4 | `CatzoSMU…` | 11,265,428.99 | 2.561% | 5% |
| 5 | `8GbwASqd…` | 10,210,832.24 | 2.321% | 0% |
| 6 | `26pV97Ce…` | 9,211,355.88 | 2.094% | 7% |
| 7 | `51JBzSTU…` | 9,144,102.43 | 2.079% | 10% |
| 8 | `9QU2QSxh…` | 7,458,789.03 | 1.696% | 7% |
| 9 | `CvSb7wdQ…` | 7,089,341.68 | 1.612% | 5% |
| 10 | `DumiCKHV…` | 6,555,721.55 | 1.49% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $118.95 |
| 24h price change | -0.12% |
| Market cap | $69,853,743,326.07022 |
| 24h volume | $4,693,232,190.049389 |
| Solana TVL | $6,498,558,714 |
| TVL 24h change | 4.72% |
| DEX volume (24h) | $3,428,858,820.75 |
| Stablecoin supply | $17,150,872,585.41 |
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