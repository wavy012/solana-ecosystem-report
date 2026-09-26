# Solana Ecosystem Report
_Generated 2026-09-26T01:06:57+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 450,522,475 |
| Current epoch | 1,042 |
| Epoch progress | 87.6% |
| Avg TPS (recent) | 4,801.0 |
| Max TPS (recent) | 5,338.92 |
| Avg slot time | 268.21 ms |
| Cluster health | ok |

## Validator status

- Active validators: **675**
- Delinquent validators: **10**
- Delinquency rate: **1.46%**
- Total active stake: **440,637,195.88 SOL**
- Median commission: **5%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,819,006.99 | 4.044% | 7% |
| 2 | `he1iusun…` | 15,817,078.8 | 3.59% | 0% |
| 3 | `3N7s9zXM…` | 12,387,903.95 | 2.811% | 0% |
| 4 | `CatzoSMU…` | 11,274,982.49 | 2.559% | 5% |
| 5 | `8GbwASqd…` | 10,595,498.78 | 2.405% | 0% |
| 6 | `26pV97Ce…` | 9,221,892.64 | 2.093% | 7% |
| 7 | `51JBzSTU…` | 9,163,087.97 | 2.08% | 10% |
| 8 | `9QU2QSxh…` | 7,599,959.38 | 1.725% | 7% |
| 9 | `CvSb7wdQ…` | 7,091,910.61 | 1.609% | 5% |
| 10 | `DumiCKHV…` | 6,557,886.69 | 1.488% | 0% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $121.77 |
| 24h price change | 3.48% |
| Market cap | $71,558,636,015.13956 |
| 24h volume | $6,416,358,263.93661 |
| Solana TVL | $6,631,924,032 |
| TVL 24h change | 3.72% |
| DEX volume (24h) | $2,509,473,542.09 |
| Stablecoin supply | $17,668,147,682.030003 |
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