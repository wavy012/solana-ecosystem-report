# Solana Ecosystem Report
_Generated 2026-10-15T18:50:01+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 457,343,476 |
| Current epoch | 1,058 |
| Epoch progress | 66.54% |
| Avg TPS (recent) | 5,331.64 |
| Max TPS (recent) | 5,878.32 |
| Avg slot time | 216.22 ms |
| Cluster health | ok |

## Validator status

- Active validators: **671**
- Delinquent validators: **9**
- Delinquency rate: **1.32%**
- Total active stake: **437,887,641.27 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,556,680.82 | 4.009% | 7% |
| 2 | `he1iusun…` | 15,475,283.77 | 3.534% | 0% |
| 3 | `3N7s9zXM…` | 12,340,405.7 | 2.818% | 0% |
| 4 | `8GbwASqd…` | 11,132,168.48 | 2.542% | 0% |
| 5 | `CatzoSMU…` | 10,777,828.96 | 2.461% | 5% |
| 6 | `51JBzSTU…` | 9,409,309.09 | 2.149% | 10% |
| 7 | `26pV97Ce…` | 9,227,344.94 | 2.107% | 7% |
| 8 | `9QU2QSxh…` | 7,737,484.48 | 1.767% | 7% |
| 9 | `CvSb7wdQ…` | 6,912,080.68 | 1.579% | 5% |
| 10 | `3JD3jMmn…` | 6,640,641.26 | 1.517% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.71 |
| 24h price change | 1.61% |
| Market cap | $62,296,472,720.962326 |
| 24h volume | $4,328,466,926.822635 |
| Solana TVL | $5,985,161,015 |
| TVL 24h change | -0.56% |
| DEX volume (24h) | $2,118,350,659.3199997 |
| Stablecoin supply | $16,062,479,588.359999 |
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