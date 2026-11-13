# Solana Ecosystem Report
_Generated 2026-11-13T17:27:32+00:00_

## Anomalies

- **[WARNING]** Validator delinquency at 5.44% (>= 5% threshold).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 469,009,652 |
| Current epoch | 1,085 |
| Epoch progress | 67.05% |
| Avg TPS (recent) | 2,055.36 |
| Max TPS (recent) | 2,387.12 |
| Avg slot time | 214.42 ms |
| Cluster health | ok |

## Validator status

- Active validators: **661**
- Delinquent validators: **38**
- Delinquency rate: **5.44%**
- Total active stake: **432,410,499.07 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 16,815,754.94 | 3.889% | 0% |
| 2 | `CcaHc2L4…` | 16,140,175.44 | 3.733% | 7% |
| 3 | `3N7s9zXM…` | 12,976,229.26 | 3.001% | 0% |
| 4 | `8GbwASqd…` | 10,117,721.9 | 2.34% | 0% |
| 5 | `51JBzSTU…` | 9,699,456.36 | 2.243% | 10% |
| 6 | `CatzoSMU…` | 9,578,398.37 | 2.215% | 5% |
| 7 | `26pV97Ce…` | 9,240,075.74 | 2.137% | 7% |
| 8 | `9QU2QSxh…` | 7,863,387.45 | 1.819% | 7% |
| 9 | `DumiCKHV…` | 6,989,060.42 | 1.616% | 0% |
| 10 | `CvSb7wdQ…` | 6,712,616.92 | 1.552% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $79.74 |
| 24h price change | -2.06% |
| Market cap | $47,152,276,372.08177 |
| 24h volume | $3,296,203,493.8133945 |
| Solana TVL | $4,942,205,418 |
| TVL 24h change | -1.86% |
| DEX volume (24h) | $1,503,485,412.77 |
| Stablecoin supply | $14,405,699,311.35 |
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