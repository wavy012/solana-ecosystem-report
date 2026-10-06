# Solana Ecosystem Report
_Generated 2026-10-06T19:38:39+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 453,997,496 |
| Current epoch | 1,050 |
| Epoch progress | 92.01% |
| Avg TPS (recent) | 5,094.78 |
| Max TPS (recent) | 5,572.88 |
| Avg slot time | 269.88 ms |
| Cluster health | ok |

## Validator status

- Active validators: **672**
- Delinquent validators: **13**
- Delinquency rate: **1.9%**
- Total active stake: **441,738,540.62 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,915,070.34 | 4.056% | 7% |
| 2 | `he1iusun…` | 15,937,333.17 | 3.608% | 0% |
| 3 | `3N7s9zXM…` | 12,292,996.65 | 2.783% | 0% |
| 4 | `8GbwASqd…` | 11,310,013.15 | 2.56% | 0% |
| 5 | `CatzoSMU…` | 11,144,637.82 | 2.523% | 5% |
| 6 | `26pV97Ce…` | 9,258,565.95 | 2.096% | 7% |
| 7 | `51JBzSTU…` | 9,254,450.06 | 2.095% | 10% |
| 8 | `9QU2QSxh…` | 7,629,485.93 | 1.727% | 7% |
| 9 | `CvSb7wdQ…` | 7,062,715.54 | 1.599% | 5% |
| 10 | `3JD3jMmn…` | 6,687,904.42 | 1.514% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $120.52 |
| 24h price change | 0.42% |
| Market cap | $70,875,941,854.95586 |
| 24h volume | $2,533,191,411.451257 |
| Solana TVL | $6,631,323,575 |
| TVL 24h change | -1.44% |
| DEX volume (24h) | $2,057,146,062.5000002 |
| Stablecoin supply | $17,029,824,007.73 |
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