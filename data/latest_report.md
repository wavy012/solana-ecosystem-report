# Solana Ecosystem Report
_Generated 2026-11-02T23:58:01+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 464,688,215 |
| Current epoch | 1,075 |
| Epoch progress | 66.72% |
| Avg TPS (recent) | 1,569.86 |
| Max TPS (recent) | 1,951.25 |
| Avg slot time | 213.91 ms |
| Cluster health | ok |

## Validator status

- Active validators: **665**
- Delinquent validators: **28**
- Delinquency rate: **4.04%**
- Total active stake: **434,160,765.87 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,034,353.88 | 3.924% | 7% |
| 2 | `he1iusun…` | 16,710,199.04 | 3.849% | 0% |
| 3 | `3N7s9zXM…` | 13,037,180.49 | 3.003% | 0% |
| 4 | `8GbwASqd…` | 10,429,501.19 | 2.402% | 0% |
| 5 | `CatzoSMU…` | 9,580,109.23 | 2.207% | 5% |
| 6 | `51JBzSTU…` | 9,453,055.22 | 2.177% | 10% |
| 7 | `26pV97Ce…` | 9,226,805.46 | 2.125% | 7% |
| 8 | `9QU2QSxh…` | 7,803,391.6 | 1.797% | 7% |
| 9 | `DumiCKHV…` | 7,001,890.81 | 1.613% | 0% |
| 10 | `CvSb7wdQ…` | 6,978,079.55 | 1.607% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $91.89 |
| 24h price change | -2.75% |
| Market cap | $54,234,450,865.954254 |
| 24h volume | $2,641,943,677.6987247 |
| Solana TVL | $5,335,089,795 |
| TVL 24h change | -1.3% |
| DEX volume (24h) | $905,602,298.19 |
| Stablecoin supply | $15,451,073,599.0 |
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