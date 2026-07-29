"""
Renders the self-contained dark-theme HTML dashboard.

Design intent (see README "Design notes" for the full rationale):
- Everything is server-rendered into one static HTML file — no CDN,
  no build step, no client-side fetch. Open it directly or serve it
  from GitHub Pages / docs/ and it just works, offline included.
- The "Network Pulse" strip is the signature element: EKG-style SVG
  sparklines of TPS and slot time drawn from real history, styled
  like a health monitor — because that's literally what this tool is
  for a live, decentralized network.
- Palette leans on Solana's own brand gradient (purple -> green) but
  only as a thin accent (pulse lines, status dots) against a near-black
  base, so it reads as "Solana's monitor," not a generic dark theme.
"""
import datetime
import html


PURPLE = "#9945FF"
GREEN = "#14F195"
BG = "#0B0B10"
PANEL = "#15151D"
BORDER = "#25252F"
TEXT = "#E7E7EE"
MUTED = "#8A8A9A"
RED = "#FF5C5C"
AMBER = "#FFB020"


def _fmt(value, suffix="", decimals=None, dash="—"):
    if value is None:
        return dash
    if decimals is not None and isinstance(value, (int, float)):
        value = round(value, decimals)
    return f"{value:,}{suffix}" if isinstance(value, (int, float)) else f"{value}{suffix}"


def _fmt_usd(value):
    if value is None:
        return "—"
    if value >= 1_000_000_000:
        return f"${value/1_000_000_000:.2f}B"
    if value >= 1_000_000:
        return f"${value/1_000_000:.2f}M"
    if value >= 1_000:
        return f"${value/1_000:.1f}K"
    return f"${value:,.2f}"


def _sparkline(values, width=220, height=48, color=GREEN):
    values = [v for v in values if isinstance(v, (int, float))]
    if len(values) < 2:
        return f'<svg width="{width}" height="{height}"></svg>'
    lo, hi = min(values), max(values)
    span = (hi - lo) or 1
    step = width / (len(values) - 1)
    points = []
    for i, v in enumerate(values):
        x = i * step
        y = height - ((v - lo) / span) * (height - 6) - 3
        points.append(f"{x:.1f},{y:.1f}")
    poly = " ".join(points)
    last_x, last_y = points[-1].split(",")
    return f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" class="sparkline">
      <polyline points="{poly}" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
      <circle cx="{last_x}" cy="{last_y}" r="3.2" fill="{color}"/>
    </svg>'''


def _severity_color(sev):
    return {"critical": RED, "warning": AMBER, "info": PURPLE}.get(sev, MUTED)


def _metric_card(label, value, sub=None):
    sub_html = f'<div class="metric-sub">{html.escape(str(sub))}</div>' if sub else ""
    return f'''<div class="metric-card">
      <div class="metric-label">{html.escape(label)}</div>
      <div class="metric-value">{html.escape(str(value))}</div>
      {sub_html}
    </div>'''


def render_dashboard(report: dict, history: list) -> str:
    perf = report.get("network_performance", {})
    validators = report.get("validator_status", {})
    econ = report.get("economic_indicators", {})
    growth = report.get("ecosystem_growth", {})
    anomalies = report.get("anomalies", [])
    roadmap = report.get("upcoming_developments", [])
    generated_at = report.get("generated_at_utc", "")
    errors = report.get("source_errors", {})

    tps_history = [h.get("network_performance", {}).get("avg_tps_recent") for h in history[-40:]] + [perf.get("avg_tps_recent")]
    slot_time_history = [h.get("network_performance", {}).get("avg_slot_time_ms") for h in history[-40:]] + [perf.get("avg_slot_time_ms")]
    price_history = [h.get("economic_indicators", {}).get("sol_price_usd") for h in history[-40:]] + [econ.get("sol_price_usd")]
    tvl_history = [h.get("economic_indicators", {}).get("solana_tvl_usd") for h in history[-40:]] + [econ.get("solana_tvl_usd")]

    anomaly_html = ""
    if anomalies:
        rows = "\n".join(
            f'''<div class="anomaly-row" style="border-left-color:{_severity_color(a["severity"])}">
                <span class="anomaly-sev" style="color:{_severity_color(a["severity"])}">{a["severity"].upper()}</span>
                <span class="anomaly-msg">{html.escape(a["message"])}</span>
            </div>'''
            for a in anomalies
        )
        anomaly_html = f'''<section class="panel">
          <h2>Anomalies detected this run</h2>
          {rows}
        </section>'''
    else:
        anomaly_html = '''<section class="panel anomaly-clear">
          <h2>Anomalies detected this run</h2>
          <div class="anomaly-row" style="border-left-color:%s">
            <span class="anomaly-sev" style="color:%s">CLEAR</span>
            <span class="anomaly-msg">No metric breached its threshold this run.</span>
          </div>
        </section>''' % (GREEN, GREEN)

    validator_rows = "\n".join(
        f'''<tr>
          <td>{i+1}</td>
          <td class="mono">{html.escape((v.get("vote_pubkey") or "")[:8])}…</td>
          <td>{_fmt(v.get("activated_stake_sol"), decimals=0)} SOL</td>
          <td>{_fmt(v.get("stake_share_pct"), suffix="%")}</td>
          <td>{_fmt(v.get("commission_pct"), suffix="%")}</td>
        </tr>'''
        for i, v in enumerate(validators.get("top_validators_by_stake", []))
    ) or '<tr><td colspan="5" class="muted">No validator data this run.</td></tr>'

    roadmap_html = "\n".join(
        f'''<div class="roadmap-item">
          <div class="roadmap-name">{html.escape(item["name"])}</div>
          <div class="roadmap-status">{html.escape(item["status"])}</div>
          <div class="roadmap-summary">{html.escape(item["summary"])}</div>
        </div>'''
        for item in roadmap
    )

    errors_html = ""
    if errors:
        items = "".join(f"<li><span class='mono'>{html.escape(k)}</span>: {html.escape(v)}</li>" for k, v in errors.items())
        errors_html = f'''<section class="panel muted-panel">
          <h2>Sources unavailable this run</h2>
          <ul class="error-list">{items}</ul>
        </section>'''

    health = perf.get("cluster_health")
    health_color = GREEN if health == "ok" else (RED if health else MUTED)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Solana Ecosystem Report</title>
<style>
  :root {{
    --bg: {BG}; --panel: {PANEL}; --border: {BORDER}; --text: {TEXT}; --muted: {MUTED};
    --purple: {PURPLE}; --green: {GREEN}; --red: {RED}; --amber: {AMBER};
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, sans-serif;
    line-height: 1.5;
  }}
  .mono {{ font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; }}
  .muted {{ color: var(--muted); }}
  header {{
    padding: 28px 32px 20px; border-bottom: 1px solid var(--border);
    background: linear-gradient(120deg, rgba(153,69,255,0.10), rgba(20,241,149,0.06));
  }}
  header .eyebrow {{ color: var(--muted); font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; }}
  header h1 {{ margin: 6px 0 4px; font-size: 26px; letter-spacing: -0.01em; }}
  header .sub {{ color: var(--muted); font-size: 13px; }}
  .health-dot {{ display:inline-block; width:8px; height:8px; border-radius:50%; background:{health_color}; margin-right:6px; }}

  main {{ max-width: 1180px; margin: 0 auto; padding: 24px 32px 64px; }}

  .pulse-strip {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }}
  .pulse-card {{ background: var(--panel); border: 1px solid var(--border); border-radius: 10px; padding: 14px 16px; }}
  .pulse-card .pulse-label {{ font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 6px; }}
  .pulse-card .pulse-value {{ font-family: "SFMono-Regular", Consolas, monospace; font-size: 20px; margin-bottom: 4px; }}
  .sparkline {{ display: block; }}

  section.panel {{ background: var(--panel); border: 1px solid var(--border); border-radius: 12px; padding: 20px 22px; margin-bottom: 20px; }}
  section.panel h2 {{ margin: 0 0 14px; font-size: 15px; letter-spacing: 0.02em; color: var(--text); }}

  .metrics-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; }}
  .metric-card {{ background: rgba(255,255,255,0.02); border: 1px solid var(--border); border-radius: 8px; padding: 12px 14px; }}
  .metric-label {{ font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.06em; }}
  .metric-value {{ font-family: "SFMono-Regular", Consolas, monospace; font-size: 19px; margin-top: 4px; }}
  .metric-sub {{ font-size: 11px; color: var(--muted); margin-top: 2px; }}

  .anomaly-row {{ border-left: 3px solid; padding: 8px 12px; margin-bottom: 8px; background: rgba(255,255,255,0.02); border-radius: 4px; display:flex; gap:10px; align-items:baseline; }}
  .anomaly-sev {{ font-size: 11px; font-weight: 700; letter-spacing: 0.06em; min-width: 64px; }}
  .anomaly-msg {{ font-size: 13px; }}

  table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  th {{ text-align: left; color: var(--muted); font-weight: 500; font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; padding: 6px 10px; border-bottom: 1px solid var(--border); }}
  td {{ padding: 8px 10px; border-bottom: 1px solid rgba(255,255,255,0.03); }}

  .roadmap-item {{ padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.03); }}
  .roadmap-item:last-child {{ border-bottom: none; }}
  .roadmap-name {{ font-weight: 600; font-size: 14px; }}
  .roadmap-status {{ font-size: 11px; color: var(--purple); text-transform: uppercase; letter-spacing: 0.05em; margin: 2px 0 4px; }}
  .roadmap-summary {{ font-size: 13px; color: var(--muted); }}

  .error-list {{ margin: 0; padding-left: 18px; font-size: 12px; color: var(--muted); }}
  .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
  footer {{ max-width: 1180px; margin: 0 auto; padding: 0 32px 40px; color: var(--muted); font-size: 12px; }}
  a {{ color: var(--green); }}
  @media (max-width: 720px) {{
    .pulse-strip {{ grid-template-columns: repeat(2, 1fr); }}
    .grid-2 {{ grid-template-columns: 1fr; }}
  }}
</style>
</head>
<body>
<header>
  <div class="eyebrow">Solana Ecosystem Report · Auto-Generated</div>
  <h1><span class="health-dot"></span>Network Pulse</h1>
  <div class="sub mono">Slot {_fmt(perf.get("current_slot"))} · Epoch {_fmt(perf.get("current_epoch"))} ({_fmt(perf.get("epoch_progress_pct"), suffix="%")} complete) · Generated {html.escape(generated_at)}</div>
</header>
<main>

  <div class="pulse-strip">
    <div class="pulse-card">
      <div class="pulse-label">TPS (recent avg)</div>
      <div class="pulse-value">{_fmt(perf.get("avg_tps_recent"))}</div>
      {_sparkline(tps_history, color=GREEN)}
    </div>
    <div class="pulse-card">
      <div class="pulse-label">Avg Slot Time</div>
      <div class="pulse-value">{_fmt(perf.get("avg_slot_time_ms"), suffix=" ms")}</div>
      {_sparkline(slot_time_history, color=PURPLE)}
    </div>
    <div class="pulse-card">
      <div class="pulse-label">SOL Price</div>
      <div class="pulse-value">{_fmt_usd(econ.get("sol_price_usd"))}</div>
      {_sparkline(price_history, color=GREEN)}
    </div>
    <div class="pulse-card">
      <div class="pulse-label">Solana TVL</div>
      <div class="pulse-value">{_fmt_usd(econ.get("solana_tvl_usd"))}</div>
      {_sparkline(tvl_history, color=PURPLE)}
    </div>
  </div>

  {anomaly_html}

  <section class="panel">
    <h2>Network performance</h2>
    <div class="metrics-grid">
      {_metric_card("Current slot", _fmt(perf.get("current_slot")))}
      {_metric_card("Current epoch", _fmt(perf.get("current_epoch")))}
      {_metric_card("Epoch progress", _fmt(perf.get("epoch_progress_pct"), suffix="%"))}
      {_metric_card("Avg TPS (recent)", _fmt(perf.get("avg_tps_recent")))}
      {_metric_card("Max TPS (recent)", _fmt(perf.get("max_tps_recent")))}
      {_metric_card("Avg slot time", _fmt(perf.get("avg_slot_time_ms"), suffix=" ms"))}
      {_metric_card("Cluster health", _fmt(perf.get("cluster_health")))}
    </div>
  </section>

  <section class="panel">
    <h2>Validator status</h2>
    <div class="metrics-grid" style="margin-bottom:16px;">
      {_metric_card("Active validators", _fmt(validators.get("active_validator_count")))}
      {_metric_card("Delinquent validators", _fmt(validators.get("delinquent_validator_count")))}
      {_metric_card("Delinquency rate", _fmt(validators.get("delinquency_pct"), suffix="%"))}
      {_metric_card("Total active stake", _fmt(validators.get("total_active_stake_sol"), decimals=0, suffix=" SOL"))}
      {_metric_card("Median commission", _fmt(validators.get("median_commission_pct"), suffix="%"))}
      {_metric_card("Zero-commission validators", _fmt(validators.get("zero_commission_validator_count")))}
    </div>
    <table>
      <thead><tr><th>#</th><th>Vote account</th><th>Stake</th><th>Share</th><th>Commission</th></tr></thead>
      <tbody>{validator_rows}</tbody>
    </table>
  </section>

  <div class="grid-2">
    <section class="panel">
      <h2>Economic indicators</h2>
      <div class="metrics-grid">
        {_metric_card("SOL price", _fmt_usd(econ.get("sol_price_usd")))}
        {_metric_card("24h change", _fmt(econ.get("sol_price_change_24h_pct"), suffix="%"))}
        {_metric_card("Market cap", _fmt_usd(econ.get("sol_market_cap_usd")))}
        {_metric_card("24h volume", _fmt_usd(econ.get("sol_24h_volume_usd")))}
        {_metric_card("Solana TVL", _fmt_usd(econ.get("solana_tvl_usd")))}
        {_metric_card("TVL 24h change", _fmt(econ.get("solana_tvl_change_24h_pct"), suffix="%"))}
        {_metric_card("DEX volume (24h)", _fmt_usd(econ.get("solana_dex_volume_24h_usd")))}
        {_metric_card("Stablecoin supply", _fmt_usd(econ.get("solana_stablecoin_supply_usd")))}
        {_metric_card("Median tx fee", _fmt(econ.get("median_tx_fee_lamports"), suffix=" lamports"))}
        {_metric_card("Est. REV / block", _fmt_usd(econ.get("estimated_rev_usd_per_block")))}
      </div>
    </section>

    <section class="panel">
      <h2>Ecosystem growth</h2>
      <div class="metrics-grid">
        {_metric_card("Tokenized equities volume", _fmt(growth.get("tokenized_equities_volume_usd")))}
        {_metric_card("Daily active addresses", _fmt(growth.get("daily_active_addresses")))}
      </div>
      <p class="muted" style="font-size:12px; margin-top:12px;">{html.escape(growth.get("note", ""))}</p>
    </section>
  </div>

  <section class="panel">
    <h2>Upcoming upgrades & developments</h2>
    {roadmap_html}
  </section>

  {errors_html}

</main>
<footer>
  Generated automatically by the Solana Ecosystem Report pipeline. Data: Solana public RPC, DeFiLlama, CoinGecko.
  See the <a href="../README.md">README</a> for methodology, refresh schedule, and known data gaps.
</footer>
</body>
</html>'''
