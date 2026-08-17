# Solana Ecosystem Report
_Generated 2026-08-17T16:53:59+00:00_

## Anomalies

- **[WARNING]** TPS spike: 5131.0 vs rolling baseline 3480.6 (47.4%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 439,887,806 |
| Current epoch | 1,018 |
| Epoch progress | 25.87% |
| Avg TPS (recent) | 5,131.0 |
| Max TPS (recent) | 7,752.95 |
| Avg slot time | 395.2 ms |
| Cluster health | ok |

## Validator status

- Active validators: **688**
- Delinquent validators: **7**
- Delinquency rate: **1.01%**
- Total active stake: **435,676,795.8 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,091,057.03 | 3.923% | 7% |
| 2 | `he1iusun…` | 16,003,006.03 | 3.673% | 0% |
| 3 | `CatzoSMU…` | 12,495,360.32 | 2.868% | 5% |
| 4 | `3N7s9zXM…` | 12,259,520.21 | 2.814% | 0% |
| 5 | `26pV97Ce…` | 9,203,435.63 | 2.112% | 7% |
| 6 | `51JBzSTU…` | 8,992,380.56 | 2.064% | 10% |
| 7 | `8GbwASqd…` | 8,305,833.8 | 1.906% | 0% |
| 8 | `9QU2QSxh…` | 7,983,993.32 | 1.833% | 7% |
| 9 | `CvSb7wdQ…` | 7,342,590.46 | 1.685% | 5% |
| 10 | `DumiCKHV…` | 6,588,036.72 | 1.512% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $75.98 |
| 24h price change | 0.67% |
| Market cap | $44,303,452,121.29024 |
| 24h volume | $1,301,904,951.091445 |
| Solana TVL | $4,844,111,010 |
| TVL 24h change | 0.73% |
| DEX volume (24h) | $1,055,467,633.95 |
| Stablecoin supply | $15,989,174,298.5 |
| Median tx fee | 5,000.0 lamports |
| Est. REV / block | $6.1783 |

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

---
_Generated automatically by the Solana Ecosystem Report pipeline. Data sources: Solana public RPC, DeFiLlama, CoinGecko._