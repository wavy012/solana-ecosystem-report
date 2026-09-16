# Solana Ecosystem Report
_Generated 2026-09-16T01:30:48+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 447,397,936 |
| Current epoch | 1,035 |
| Epoch progress | 64.33% |
| Avg TPS (recent) | 5,045.14 |
| Max TPS (recent) | 5,493.3 |
| Avg slot time | 319.75 ms |
| Cluster health | ok |

## Validator status

- Active validators: **677**
- Delinquent validators: **12**
- Delinquency rate: **1.74%**
- Total active stake: **439,248,639.21 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,757,711.87 | 4.043% | 7% |
| 2 | `he1iusun…` | 16,373,376.88 | 3.728% | 0% |
| 3 | `3N7s9zXM…` | 12,492,604.95 | 2.844% | 0% |
| 4 | `CatzoSMU…` | 11,369,566.14 | 2.588% | 5% |
| 5 | `8GbwASqd…` | 9,669,319.45 | 2.201% | 0% |
| 6 | `26pV97Ce…` | 9,256,224.98 | 2.107% | 7% |
| 7 | `51JBzSTU…` | 9,035,102.59 | 2.057% | 10% |
| 8 | `9QU2QSxh…` | 7,372,354.85 | 1.678% | 7% |
| 9 | `CvSb7wdQ…` | 6,944,775.01 | 1.581% | 5% |
| 10 | `DumiCKHV…` | 6,553,625.65 | 1.492% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $97.09 |
| 24h price change | -4.98% |
| Market cap | $56,997,825,654.26669 |
| 24h volume | $3,864,793,998.797791 |
| Solana TVL | $5,722,142,855 |
| TVL 24h change | -1.95% |
| DEX volume (24h) | $2,410,890,436.0099998 |
| Stablecoin supply | $15,946,406,232.42 |
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