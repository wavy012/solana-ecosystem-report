# Solana Ecosystem Report
_Generated 2026-10-29T06:08:34+00:00_

## Anomalies

- No metric breached its threshold this run.

## Network performance

| Metric | Value |
|---|---|
| Current slot | 462,774,270 |
| Current epoch | 1,071 |
| Epoch progress | 23.67% |
| Avg TPS (recent) | 1,249.17 |
| Max TPS (recent) | 2,051.88 |
| Avg slot time | 213.64 ms |
| Cluster health | ok |

## Validator status

- Active validators: **666**
- Delinquent validators: **23**
- Delinquency rate: **3.34%**
- Total active stake: **436,776,187.41 SOL**
- Median commission: **5.0%**

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L4…` | 17,028,574.24 | 3.899% | 7% |
| 2 | `he1iusun…` | 16,665,444.38 | 3.816% | 0% |
| 3 | `3N7s9zXM…` | 12,878,826.06 | 2.949% | 0% |
| 4 | `8GbwASqd…` | 10,762,072.57 | 2.464% | 0% |
| 5 | `CatzoSMU…` | 9,705,355.84 | 2.222% | 5% |
| 6 | `51JBzSTU…` | 9,466,645.88 | 2.167% | 10% |
| 7 | `26pV97Ce…` | 9,218,109.83 | 2.11% | 7% |
| 8 | `9QU2QSxh…` | 7,761,554.6 | 1.777% | 7% |
| 9 | `DumiCKHV…` | 6,998,037.17 | 1.602% | 0% |
| 10 | `CvSb7wdQ…` | 6,646,427.91 | 1.522% | 5% |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $100.29 |
| 24h price change | -1.49% |
| Market cap | $59,189,558,681.4493 |
| 24h volume | $2,936,303,349.705043 |
| Solana TVL | $5,640,499,198 |
| TVL 24h change | -0.93% |
| DEX volume (24h) | $1,624,512,203.0600002 |
| Stablecoin supply | $15,698,622,067.6 |
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