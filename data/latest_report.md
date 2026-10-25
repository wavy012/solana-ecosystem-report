# Solana Ecosystem Report
_Generated 2026-10-25T22:42:55+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 461,430,917 |
| Current epoch | 1,068 |
| Epoch progress | 12.71% |
| Avg TPS (recent) | 1,897.58 |
| Max TPS (recent) | 2,281.13 |
| Avg slot time | 212.71 ms |
| Cluster health | ok |

## Validator status

- Active validators: **665**
- Delinquent validators: **25**
- Delinquency rate: **3.62%**
- Total active stake: **437,716,745.93 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,102,487.44 | 3.907% | 7% |
| 2 | `he1iusun…` | 16,635,522.72 | 3.801% | 0% |
| 3 | `3N7s9zXM…` | 12,594,585.3 | 2.877% | 0% |
| 4 | `8GbwASqd…` | 10,882,967.43 | 2.486% | 0% |
| 5 | `CatzoSMU…` | 9,720,519.99 | 2.221% | 5% |
| 6 | `51JBzSTU…` | 9,492,381.78 | 2.169% | 10% |
| 7 | `26pV97Ce…` | 9,187,388.15 | 2.099% | 7% |
| 8 | `9QU2QSxh…` | 7,787,017.53 | 1.779% | 7% |
| 9 | `CvSb7wdQ…` | 7,039,208.64 | 1.608% | 5% |
| 10 | `DumiCKHV…` | 6,989,716.37 | 1.597% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $101.59 |
| 24h price change | 0.02% |
| Market cap | $59,918,493,009.54223 |
| 24h volume | $1,447,047,862.9054997 |
| Solana TVL | $5,734,124,889 |
| TVL 24h change | -0.71% |
| DEX volume (24h) | $1,423,041,369.8 |
| Stablecoin supply | $15,937,418,669.58 |
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