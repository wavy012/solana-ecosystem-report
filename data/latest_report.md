# Solana Ecosystem Report
_Generated 2026-11-01T10:58:37+00:00_

## Anomalies

- **[WARNING]** TPS drop: 1048.1 vs rolling baseline 1667.31 (-37.1%).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 464,066,927 |
| Current epoch | 1,074 |
| Epoch progress | 22.9% |
| Avg TPS (recent) | 1,048.1 |
| Max TPS (recent) | 1,327.13 |
| Avg slot time | 213.12 ms |
| Cluster health | ok |

## Validator status

- Active validators: **663**
- Delinquent validators: **33**
- Delinquency rate: **4.74%**
- Total active stake: **433,943,288.46 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,029,196.29 | 3.924% | 7% |
| 2 | `he1iusun…` | 16,695,127.02 | 3.847% | 0% |
| 3 | `3N7s9zXM…` | 12,943,199.27 | 2.983% | 0% |
| 4 | `8GbwASqd…` | 10,426,987.44 | 2.403% | 0% |
| 5 | `CatzoSMU…` | 9,583,156.9 | 2.208% | 5% |
| 6 | `51JBzSTU…` | 9,451,196.6 | 2.178% | 10% |
| 7 | `26pV97Ce…` | 9,225,052.85 | 2.126% | 7% |
| 8 | `9QU2QSxh…` | 7,791,638.52 | 1.796% | 7% |
| 9 | `DumiCKHV…` | 7,001,293.41 | 1.613% | 0% |
| 10 | `CvSb7wdQ…` | 6,977,107.96 | 1.608% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.33 |
| 24h price change | -0.19% |
| Market cap | $56,256,760,251.06611 |
| 24h volume | $1,190,190,473.4304643 |
| Solana TVL | $5,414,500,608 |
| TVL 24h change | -0.66% |
| DEX volume (24h) | $953,373,035.19 |
| Stablecoin supply | $15,515,805,576.339998 |
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