# Solana Ecosystem Report
_Generated 2026-10-17T17:41:56+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 458,123,155 |
| Current epoch | 1,060 |
| Epoch progress | 47.02% |
| Avg TPS (recent) | 5,059.41 |
| Max TPS (recent) | 5,517.5 |
| Avg slot time | 216.84 ms |
| Cluster health | ok |

## Validator status

- Active validators: **670**
- Delinquent validators: **11**
- Delinquency rate: **1.62%**
- Total active stake: **438,750,364.88 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,532,932.52 | 3.996% | 7% |
| 2 | `he1iusun…` | 15,736,568.13 | 3.587% | 0% |
| 3 | `3N7s9zXM…` | 12,486,161.32 | 2.846% | 0% |
| 4 | `8GbwASqd…` | 10,972,882.76 | 2.501% | 0% |
| 5 | `CatzoSMU…` | 10,191,941.77 | 2.323% | 5% |
| 6 | `51JBzSTU…` | 9,445,787.33 | 2.153% | 10% |
| 7 | `26pV97Ce…` | 9,250,229.49 | 2.108% | 7% |
| 8 | `9QU2QSxh…` | 7,759,724.0 | 1.769% | 7% |
| 9 | `CvSb7wdQ…` | 6,991,826.98 | 1.594% | 5% |
| 10 | `DumiCKHV…` | 6,726,220.22 | 1.533% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.28 |
| 24h price change | -1.04% |
| Market cap | $60,827,666,424.18828 |
| 24h volume | $1,775,337,348.1662202 |
| Solana TVL | $5,904,149,029 |
| TVL 24h change | -1.35% |
| DEX volume (24h) | $2,168,129,752.12 |
| Stablecoin supply | $16,036,133,468.91 |
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