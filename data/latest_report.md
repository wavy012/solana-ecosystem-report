# Solana Ecosystem Report
_Generated 2026-08-19T17:22:24+00:00_

## Anomalies

- **[WARNING]** TPS spike: 5333.02 vs rolling baseline 3961.47 (34.6%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 440,307,640 |
| Current epoch | 1,019 |
| Epoch progress | 23.06% |
| Avg TPS (recent) | 5,333.02 |
| Max TPS (recent) | 6,183.95 |
| Avg slot time | 416.73 ms |
| Cluster health | ok |

## Validator status

- Active validators: **686**
- Delinquent validators: **9**
- Delinquency rate: **1.29%**
- Total active stake: **435,241,267.84 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,101,526.86 | 3.929% | 7% |
| 2 | `he1iusun…` | 16,011,570.34 | 3.679% | 0% |
| 3 | `CatzoSMU…` | 12,410,377.83 | 2.851% | 5% |
| 4 | `3N7s9zXM…` | 12,198,972.14 | 2.803% | 0% |
| 5 | `26pV97Ce…` | 9,188,631.12 | 2.111% | 7% |
| 6 | `51JBzSTU…` | 8,991,289.76 | 2.066% | 10% |
| 7 | `8GbwASqd…` | 8,308,413.01 | 1.909% | 0% |
| 8 | `9QU2QSxh…` | 7,991,430.5 | 1.836% | 7% |
| 9 | `CvSb7wdQ…` | 7,344,654.5 | 1.687% | 5% |
| 10 | `DumiCKHV…` | 6,546,145.69 | 1.504% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $81.09 |
| 24h price change | 5.42% |
| Market cap | $47,275,639,770.86022 |
| 24h volume | $2,872,624,127.1978965 |
| Solana TVL | $5,054,170,251 |
| TVL 24h change | 4.22% |
| DEX volume (24h) | $1,838,194,723.04 |
| Stablecoin supply | $15,994,521,920.57 |
| Median tx fee | 5,003 lamports |
| Est. REV / block | $6.2873 |

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