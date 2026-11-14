# Solana Ecosystem Report
_Generated 2026-11-14T02:51:55+00:00_

## Anomalies

- **[WARNING]** Validator delinquency at 5.15% (>= 5% threshold).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 469,166,973 |
| Current epoch | 1,086 |
| Epoch progress | 3.47% |
| Avg TPS (recent) | 2,176.85 |
| Max TPS (recent) | 3,454.9 |
| Avg slot time | 215.29 ms |
| Cluster health | ok |

## Validator status

- Active validators: **663**
- Delinquent validators: **36**
- Delinquency rate: **5.15%**
- Total active stake: **429,651,630.95 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 16,955,905.04 | 3.946% | 0% |
| 2 | `CcaHc2L4…` | 16,374,908.88 | 3.811% | 7% |
| 3 | `3N7s9zXM…` | 12,611,498.27 | 2.935% | 0% |
| 4 | `8GbwASqd…` | 10,140,468.47 | 2.36% | 0% |
| 5 | `51JBzSTU…` | 9,736,889.59 | 2.266% | 10% |
| 6 | `CatzoSMU…` | 9,574,439.09 | 2.228% | 5% |
| 7 | `26pV97Ce…` | 9,199,377.38 | 2.141% | 7% |
| 8 | `9QU2QSxh…` | 7,914,792.05 | 1.842% | 7% |
| 9 | `DumiCKHV…` | 6,990,062.04 | 1.627% | 0% |
| 10 | `CvSb7wdQ…` | 6,707,744.9 | 1.561% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $76.0 |
| 24h price change | -5.08% |
| Market cap | $44,958,667,565.726906 |
| 24h volume | $3,806,733,226.1162834 |
| Solana TVL | $4,867,728,291 |
| TVL 24h change | -1.0% |
| DEX volume (24h) | $1,453,256,848.2 |
| Stablecoin supply | $14,255,798,493.57 |
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