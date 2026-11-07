# Solana Ecosystem Report
_Generated 2026-11-07T20:23:03+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 466,645,017 |
| Current epoch | 1,080 |
| Epoch progress | 19.68% |
| Avg TPS (recent) | 1,807.77 |
| Max TPS (recent) | 2,361.12 |
| Avg slot time | 214.95 ms |
| Cluster health | ok |

## Validator status

- Active validators: **663**
- Delinquent validators: **34**
- Delinquency rate: **4.88%**
- Total active stake: **434,780,964.77 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,043,402.15 | 3.92% | 7% |
| 2 | `he1iusun…` | 16,729,015.58 | 3.848% | 0% |
| 3 | `3N7s9zXM…` | 13,015,290.67 | 2.994% | 0% |
| 4 | `8GbwASqd…` | 10,277,562.55 | 2.364% | 0% |
| 5 | `CatzoSMU…` | 9,558,411.28 | 2.198% | 5% |
| 6 | `51JBzSTU…` | 9,520,069.59 | 2.19% | 10% |
| 7 | `26pV97Ce…` | 9,242,930.18 | 2.126% | 7% |
| 8 | `9QU2QSxh…` | 7,750,589.2 | 1.783% | 7% |
| 9 | `CvSb7wdQ…` | 6,983,623.27 | 1.606% | 5% |
| 10 | `DumiCKHV…` | 6,973,337.25 | 1.604% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $89.49 |
| 24h price change | -0.59% |
| Market cap | $52,893,396,635.237076 |
| 24h volume | $912,154,822.3236793 |
| Solana TVL | $5,203,599,036 |
| TVL 24h change | -1.08% |
| DEX volume (24h) | $1,479,986,839.85 |
| Stablecoin supply | $15,083,123,760.26 |
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