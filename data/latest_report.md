# Solana Ecosystem Report
_Generated 2026-09-30T02:14:09+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 451,826,650 |
| Current epoch | 1,045 |
| Epoch progress | 89.5% |
| Avg TPS (recent) | 4,111.84 |
| Max TPS (recent) | 4,473.05 |
| Avg slot time | 267.03 ms |
| Cluster health | ok |

## Validator status

- Active validators: **675**
- Delinquent validators: **8**
- Delinquency rate: **1.17%**
- Total active stake: **441,249,792.17 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,824,525.22 | 4.04% | 7% |
| 2 | `he1iusun…` | 15,886,037.99 | 3.6% | 0% |
| 3 | `3N7s9zXM…` | 12,338,576.59 | 2.796% | 0% |
| 4 | `8GbwASqd…` | 11,300,554.37 | 2.561% | 0% |
| 5 | `CatzoSMU…` | 11,209,854.78 | 2.54% | 5% |
| 6 | `26pV97Ce…` | 9,243,744.06 | 2.095% | 7% |
| 7 | `51JBzSTU…` | 9,224,466.33 | 2.091% | 10% |
| 8 | `9QU2QSxh…` | 7,637,467.56 | 1.731% | 7% |
| 9 | `CvSb7wdQ…` | 6,700,082.91 | 1.518% | 5% |
| 10 | `DumiCKHV…` | 6,518,406.52 | 1.477% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $119.72 |
| 24h price change | 2.43% |
| Market cap | $70,388,236,206.99992 |
| 24h volume | $3,481,270,670.5489035 |
| Solana TVL | $6,566,724,710 |
| TVL 24h change | -1.09% |
| DEX volume (24h) | $2,660,711,114.8400006 |
| Stablecoin supply | $16,454,350,024.990002 |
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