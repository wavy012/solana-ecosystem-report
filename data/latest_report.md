# Solana Ecosystem Report
_Generated 2026-11-26T15:33:21+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 474,199,742 |
| Current epoch | 1,097 |
| Epoch progress | 68.46% |
| Avg TPS (recent) | 2,114.67 |
| Max TPS (recent) | 3,364.4 |
| Avg slot time | 216.09 ms |
| Cluster health | ok |

## Validator status

- Active validators: **657**
- Delinquent validators: **31**
- Delinquency rate: **4.51%**
- Total active stake: **423,675,927.38 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 16,804,999.61 | 3.966% | 0% |
| 2 | `CcaHc2L4…` | 15,814,430.69 | 3.733% | 7% |
| 3 | `3N7s9zXM…` | 12,430,859.16 | 2.934% | 0% |
| 4 | `8GbwASqd…` | 10,236,589.18 | 2.416% | 0% |
| 5 | `51JBzSTU…` | 9,910,258.21 | 2.339% | 10% |
| 6 | `CatzoSMU…` | 9,615,393.62 | 2.27% | 5% |
| 7 | `26pV97Ce…` | 9,281,562.76 | 2.191% | 7% |
| 8 | `9QU2QSxh…` | 8,032,075.36 | 1.896% | 7% |
| 9 | `DumiCKHV…` | 6,971,305.27 | 1.645% | 0% |
| 10 | `CvSb7wdQ…` | 6,740,286.56 | 1.591% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.52 |
| 24h price change | 5.47% |
| Market cap | $41,759,682,715.1108 |
| 24h volume | $2,586,413,261.9147863 |
| Solana TVL | $4,591,235,949 |
| TVL 24h change | 1.53% |
| DEX volume (24h) | $1,511,024,370.7999997 |
| Stablecoin supply | $13,365,085,540.74 |
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