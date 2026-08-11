# Solana Ecosystem Report
_Generated 2026-08-11T20:47:30+00:00_

## Anomalies

- **[WARNING]** TPS spike: 4748.09 vs rolling baseline 3570.71 (33.0%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 438,677,362 |
| Current epoch | 1,015 |
| Epoch progress | 45.68% |
| Avg TPS (recent) | 4,748.09 |
| Max TPS (recent) | 5,256.55 |
| Avg slot time | 424.06 ms |
| Cluster health | ok |

## Validator status

- Active validators: **688**
- Delinquent validators: **11**
- Delinquency rate: **1.57%**
- Total active stake: **434,931,020.52 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 16,988,467.78 | 3.906% | 7% |
| 2 | `he1iusun…` | 15,978,711.02 | 3.674% | 0% |
| 3 | `CatzoSMU…` | 12,495,007.4 | 2.873% | 5% |
| 4 | `3N7s9zXM…` | 12,334,140.28 | 2.836% | 0% |
| 5 | `26pV97Ce…` | 9,151,704.97 | 2.104% | 7% |
| 6 | `51JBzSTU…` | 8,964,622.24 | 2.061% | 10% |
| 7 | `8GbwASqd…` | 8,172,870.67 | 1.879% | 0% |
| 8 | `9QU2QSxh…` | 7,954,158.02 | 1.829% | 7% |
| 9 | `CvSb7wdQ…` | 7,367,683.93 | 1.694% | 5% |
| 10 | `DumiCKHV…` | 6,577,941.01 | 1.512% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $75.9 |
| 24h price change | -0.61% |
| Market cap | $44,207,767,141.2006 |
| 24h volume | $1,306,960,849.619351 |
| Solana TVL | $4,797,389,128 |
| TVL 24h change | -0.83% |
| DEX volume (24h) | $1,581,973,855.56 |
| Stablecoin supply | $16,307,658,798.720001 |
| Median tx fee | 5,000.0 lamports |
| Est. REV / block | $2.7717 |

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