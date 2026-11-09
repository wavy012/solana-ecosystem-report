# Solana Ecosystem Report
_Generated 2026-11-09T07:33:04+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 467,234,935 |
| Current epoch | 1,081 |
| Epoch progress | 56.23% |
| Avg TPS (recent) | 1,304.31 |
| Max TPS (recent) | 1,796.77 |
| Avg slot time | 214.62 ms |
| Cluster health | ok |

## Validator status

- Active validators: **663**
- Delinquent validators: **34**
- Delinquency rate: **4.88%**
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
| SOL price | $85.31 |
| 24h price change | -4.14% |
| Market cap | $50,423,954,976.02009 |
| 24h volume | $2,375,391,277.751808 |
| Solana TVL | $5,088,887,927 |
| TVL 24h change | -1.8% |
| DEX volume (24h) | $997,094,322.3000001 |
| Stablecoin supply | $15,096,512,387.77 |
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