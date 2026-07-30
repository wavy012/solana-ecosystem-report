# Solana Ecosystem Report
_Generated 2026-07-30T00:07:40+00:00_

## Anomalies

- **[CRITICAL]** TPS drop: 3243.34 vs rolling baseline 24204.51 (-86.6%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 436,046,393 |
| Current epoch | 1,009 |
| Epoch progress | 36.66% |
| Avg TPS (recent) | 3,243.34 |
| Max TPS (recent) | 3,969.42 |
| Avg slot time | 422.09 ms |
| Cluster health | ok |

## Validator status

- Active validators: **693**
- Delinquent validators: **12**
- Delinquency rate: **1.7%**
- Total active stake: **428,355,204.47 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 16,884,686.62 | 3.942% | 7% |
| 2 | `he1iusun…` | 15,936,000.65 | 3.72% | 0% |
| 3 | `CatzoSMU…` | 12,514,279.74 | 2.921% | 5% |
| 4 | `3N7s9zXM…` | 12,205,908.25 | 2.849% | 0% |
| 5 | `26pV97Ce…` | 9,211,312.28 | 2.15% | 7% |
| 6 | `51JBzSTU…` | 8,236,625.47 | 1.923% | 10% |
| 7 | `8GbwASqd…` | 8,148,575.89 | 1.902% | 0% |
| 8 | `9QU2QSxh…` | 7,637,416.02 | 1.783% | 7% |
| 9 | `CvSb7wdQ…` | 6,798,605.04 | 1.587% | 5% |
| 10 | `DumiCKHV…` | 6,632,406.76 | 1.548% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $73.62 |
| 24h price change | -0.43% |
| Market cap | $42,655,960,858.29583 |
| 24h volume | $1,727,021,727.7204785 |
| Solana TVL | $4,759,304,894 |
| TVL 24h change | -0.9% |
| DEX volume (24h) | $1,736,687,117.1499999 |
| Stablecoin supply | $16,168,726,782.560001 |
| Median tx fee | 5,001.0 lamports |
| Est. REV / block | $1.2875 |

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