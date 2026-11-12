# Solana Ecosystem Report
_Generated 2026-11-12T05:46:10+00:00_

## Anomalies

- **[WARNING]** Validator delinquency at 5.3% (>= 5% threshold).

## Network performance

| Metric | Value |
|---|---|
| Current slot | 468,412,980 |
| Current epoch | 1,084 |
| Epoch progress | 28.93% |
| Avg TPS (recent) | 1,467.36 |
| Max TPS (recent) | 2,131.12 |
| Avg slot time | 214.63 ms |
| Cluster health | ok |

## Validator status

- Active validators: **661**
- Delinquent validators: **37**
- Delinquency rate: **5.3%**
- Total active stake: **433,416,361.13 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusun…` | 16,789,054.44 | 3.874% | 0% |
| 2 | `CcaHc2L4…` | 16,119,193.94 | 3.719% | 7% |
| 3 | `3N7s9zXM…` | 13,026,247.05 | 3.005% | 0% |
| 4 | `8GbwASqd…` | 10,116,092.21 | 2.334% | 0% |
| 5 | `51JBzSTU…` | 9,681,376.09 | 2.234% | 10% |
| 6 | `CatzoSMU…` | 9,580,180.03 | 2.21% | 5% |
| 7 | `26pV97Ce…` | 9,230,504.21 | 2.13% | 7% |
| 8 | `9QU2QSxh…` | 7,840,792.33 | 1.809% | 7% |
| 9 | `DumiCKHV…` | 6,987,981.2 | 1.612% | 0% |
| 10 | `CvSb7wdQ…` | 6,730,420.5 | 1.553% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $82.85 |
| 24h price change | -0.27% |
| Market cap | $49,010,715,146.7071 |
| 24h volume | $2,100,206,360.4993525 |
| Solana TVL | $5,024,379,848 |
| TVL 24h change | -0.02% |
| DEX volume (24h) | $1,636,935,274.95 |
| Stablecoin supply | $14,254,952,823.75 |
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