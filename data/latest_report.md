# Solana Ecosystem Report
_Generated 2026-09-16T17:25:32+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 447,578,895 |
| Current epoch | 1,036 |
| Epoch progress | 6.22% |
| Avg TPS (recent) | 4,442.29 |
| Max TPS (recent) | 5,000.17 |
| Avg slot time | 316.81 ms |
| Cluster health | ok |

## Validator status

- Active validators: **677**
- Delinquent validators: **14**
- Delinquency rate: **2.03%**
- Total active stake: **439,761,082.74 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,767,427.7 | 4.04% | 7% |
| 2 | `he1iusun…` | 16,352,114.4 | 3.718% | 0% |
| 3 | `3N7s9zXM…` | 12,485,145.26 | 2.839% | 0% |
| 4 | `CatzoSMU…` | 11,383,246.87 | 2.589% | 5% |
| 5 | `8GbwASqd…` | 9,740,877.34 | 2.215% | 0% |
| 6 | `26pV97Ce…` | 9,256,273.09 | 2.105% | 7% |
| 7 | `51JBzSTU…` | 9,049,051.49 | 2.058% | 10% |
| 8 | `9QU2QSxh…` | 7,386,183.49 | 1.68% | 7% |
| 9 | `CvSb7wdQ…` | 7,076,306.41 | 1.609% | 5% |
| 10 | `DumiCKHV…` | 6,558,592.36 | 1.491% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $96.94 |
| 24h price change | -2.15% |
| Market cap | $56,901,361,757.561325 |
| 24h volume | $3,545,718,930.2374644 |
| Solana TVL | $5,706,392,665 |
| TVL 24h change | -3.59% |
| DEX volume (24h) | $2,703,297,666.22 |
| Stablecoin supply | $15,946,406,232.42 |
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