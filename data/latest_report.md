# Solana Ecosystem Report
_Generated 2026-11-09T00:36:22+00:00_

## Anomalies

- **[WARNING]** Validator delinquency at 5.16% (>= 5% threshold).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 467,118,501 |
| Current epoch | 1,081 |
| Epoch progress | 29.28% |
| Avg TPS (recent) | 1,764.53 |
| Max TPS (recent) | 2,330.77 |
| Avg slot time | 214.97 ms |
| Cluster health | ok |

## Validator status

- Active validators: **661**
- Delinquent validators: **36**
- Delinquency rate: **5.16%**
- Total active stake: **433,920,560.63 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,050,552.56 | 3.929% | 7% |
| 2 | `he1iusun…` | 16,720,131.04 | 3.853% | 0% |
| 3 | `3N7s9zXM…` | 13,021,912.46 | 3.001% | 0% |
| 4 | `8GbwASqd…` | 10,279,070.04 | 2.369% | 0% |
| 5 | `CatzoSMU…` | 9,553,388.11 | 2.202% | 5% |
| 6 | `51JBzSTU…` | 9,550,278.2 | 2.201% | 10% |
| 7 | `26pV97Ce…` | 9,222,876.15 | 2.125% | 7% |
| 8 | `9QU2QSxh…` | 7,775,136.55 | 1.792% | 7% |
| 9 | `DumiCKHV…` | 6,980,318.8 | 1.609% | 0% |
| 10 | `CvSb7wdQ…` | 6,711,283.53 | 1.547% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $87.09 |
| 24h price change | -2.55% |
| Market cap | $51,402,024,939.192116 |
| 24h volume | $1,885,205,885.488981 |
| Solana TVL | $5,105,006,777 |
| TVL 24h change | -2.31% |
| DEX volume (24h) | $917,438,831.6099999 |
| Stablecoin supply | $15,177,858,508.23 |
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