# Solana Ecosystem Report
_Generated 2026-10-10T21:00:53+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 455,395,981 |
| Current epoch | 1,054 |
| Epoch progress | 15.73% |
| Avg TPS (recent) | 4,756.89 |
| Max TPS (recent) | 5,133.08 |
| Avg slot time | 217.47 ms |
| Cluster health | ok |

## Validator status

- Active validators: **674**
- Delinquent validators: **6**
- Delinquency rate: **0.88%**
- Total active stake: **438,737,964.33 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,775,444.15 | 4.051% | 7% |
| 2 | `he1iusun…` | 15,954,956.57 | 3.637% | 0% |
| 3 | `3N7s9zXM…` | 12,313,355.73 | 2.807% | 0% |
| 4 | `8GbwASqd…` | 11,145,933.52 | 2.54% | 0% |
| 5 | `CatzoSMU…` | 10,754,664.23 | 2.451% | 5% |
| 6 | `51JBzSTU…` | 9,328,688.51 | 2.126% | 10% |
| 7 | `26pV97Ce…` | 9,240,265.58 | 2.106% | 7% |
| 8 | `9QU2QSxh…` | 7,603,785.75 | 1.733% | 7% |
| 9 | `CvSb7wdQ…` | 6,810,142.07 | 1.552% | 5% |
| 10 | `3JD3jMmn…` | 6,421,774.32 | 1.464% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $110.3 |
| 24h price change | 1.25% |
| Market cap | $64,947,775,227.61848 |
| 24h volume | $1,566,363,964.6545887 |
| Solana TVL | $6,218,556,521 |
| TVL 24h change | 0.11% |
| DEX volume (24h) | $1,978,097,665.9099998 |
| Stablecoin supply | $16,409,904,507.15 |
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