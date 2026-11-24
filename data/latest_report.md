# Solana Ecosystem Report
_Generated 2026-11-24T11:28:03+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 473,327,540 |
| Current epoch | 1,095 |
| Epoch progress | 66.56% |
| Avg TPS (recent) | 1,662.36 |
| Max TPS (recent) | 2,738.77 |
| Avg slot time | 215.87 ms |
| Cluster health | ok |

## Validator status

- Active validators: **660**
- Delinquent validators: **26**
- Delinquency rate: **3.79%**
- Total active stake: **425,856,003.65 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 17,028,046.2 | 3.999% | 0% |
| 2 | `CcaHc2L4…` | 16,091,420.43 | 3.779% | 7% |
| 3 | `3N7s9zXM…` | 12,412,157.56 | 2.915% | 0% |
| 4 | `8GbwASqd…` | 10,240,508.08 | 2.405% | 0% |
| 5 | `51JBzSTU…` | 9,856,365.99 | 2.314% | 10% |
| 6 | `CatzoSMU…` | 9,634,021.97 | 2.262% | 5% |
| 7 | `26pV97Ce…` | 9,276,353.71 | 2.178% | 7% |
| 8 | `9QU2QSxh…` | 8,005,660.3 | 1.88% | 7% |
| 9 | `DumiCKHV…` | 6,987,775.67 | 1.641% | 0% |
| 10 | `CvSb7wdQ…` | 6,778,434.27 | 1.592% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.16 |
| 24h price change | -3.14% |
| Market cap | $42,014,902,173.61836 |
| 24h volume | $3,689,925,182.320644 |
| Solana TVL | $4,596,422,717 |
| TVL 24h change | -0.46% |
| DEX volume (24h) | $1,403,428,541.26 |
| Stablecoin supply | $13,918,367,981.949999 |
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