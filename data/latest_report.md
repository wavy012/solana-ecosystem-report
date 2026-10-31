# Solana Ecosystem Report
_Generated 2026-10-31T17:28:46+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 463,772,637 |
| Current epoch | 1,073 |
| Epoch progress | 54.78% |
| Avg TPS (recent) | 1,604.35 |
| Max TPS (recent) | 2,129.18 |
| Avg slot time | 214.64 ms |
| Cluster health | ok |

## Validator status

- Active validators: **665**
- Delinquent validators: **27**
- Delinquency rate: **3.9%**
- Total active stake: **433,649,347.15 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,020,574.15 | 3.925% | 7% |
| 2 | `he1iusun…` | 16,688,714.62 | 3.848% | 0% |
| 3 | `3N7s9zXM…` | 12,931,864.01 | 2.982% | 0% |
| 4 | `8GbwASqd…` | 10,425,467.08 | 2.404% | 0% |
| 5 | `CatzoSMU…` | 9,651,671.1 | 2.226% | 5% |
| 6 | `51JBzSTU…` | 9,449,480.63 | 2.179% | 10% |
| 7 | `26pV97Ce…` | 9,227,526.32 | 2.128% | 7% |
| 8 | `9QU2QSxh…` | 7,778,595.05 | 1.794% | 7% |
| 9 | `DumiCKHV…` | 7,000,337.73 | 1.614% | 0% |
| 10 | `CvSb7wdQ…` | 6,976,145.23 | 1.609% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.94 |
| 24h price change | 1.23% |
| Market cap | $56,613,082,822.48639 |
| 24h volume | $2,204,162,709.3669786 |
| Solana TVL | $5,419,703,702 |
| TVL 24h change | 1.44% |
| DEX volume (24h) | $2,117,396,479.19 |
| Stablecoin supply | $15,496,762,370.87 |
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