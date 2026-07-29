"""
Anomaly detection for the Solana ecosystem report.

Design choice: explainable rules over a rolling baseline, not a black-box
model. Every anomaly the report flags comes with the exact rule and
numbers that tripped it, so a human can immediately judge whether it's
real or noise. Two kinds of checks:

1. Rolling-baseline deviation (TPS, TVL, price) — compares "now" against
   the mean of the last N snapshots this pipeline has collected.
2. Absolute thresholds (slot time, delinquency %) — compares "now"
   against a fixed, documented ceiling, since these have a known-good
   range regardless of history.
"""
import statistics

from . import config


def _pct_change(current, baseline):
    if current is None or baseline in (None, 0):
        return None
    return 100 * (current - baseline) / baseline


def _rolling_mean(history: list, key_path, window: int):
    values = []
    for snap in history[-window:]:
        v = snap
        for key in key_path:
            if not isinstance(v, dict):
                v = None
                break
            v = v.get(key)
        if isinstance(v, (int, float)):
            values.append(v)
    return statistics.mean(values) if values else None


def detect_anomalies(current_report: dict, history: list) -> list:
    """
    `current_report` is this run's full report dict (before it's appended
    to history). `history` is the list of previously saved snapshots
    (oldest first), NOT including the current one.
    Returns a list of anomaly dicts: {metric, severity, message, value, baseline_or_threshold}.
    """
    thresholds = config.ANOMALY_THRESHOLDS
    window = config.ANOMALY_ROLLING_WINDOW
    anomalies = []

    perf = current_report.get("network_performance", {})
    validators = current_report.get("validator_status", {})
    econ = current_report.get("economic_indicators", {})

    # --- TPS deviation vs rolling mean ---
    tps_now = perf.get("avg_tps_recent")
    tps_baseline = _rolling_mean(history, ["network_performance", "avg_tps_recent"], window)
    tps_dev = _pct_change(tps_now, tps_baseline)
    if tps_dev is not None and abs(tps_dev) >= thresholds["tps_deviation_pct"]:
        direction = "spike" if tps_dev > 0 else "drop"
        anomalies.append({
            "metric": "avg_tps_recent",
            "severity": "warning" if abs(tps_dev) < 2 * thresholds["tps_deviation_pct"] else "critical",
            "message": f"TPS {direction}: {tps_now} vs rolling baseline {round(tps_baseline, 2)} ({round(tps_dev, 1)}%).",
            "value": tps_now,
            "baseline": round(tps_baseline, 2),
            "deviation_pct": round(tps_dev, 1),
        })

    # --- Slot time absolute threshold ---
    slot_time_now = perf.get("avg_slot_time_ms")
    if slot_time_now is not None and slot_time_now >= thresholds["slot_time_ms_max"]:
        anomalies.append({
            "metric": "avg_slot_time_ms",
            "severity": "warning",
            "message": f"Average slot time {slot_time_now}ms is above the {thresholds['slot_time_ms_max']}ms ceiling — network may be congested.",
            "value": slot_time_now,
            "threshold": thresholds["slot_time_ms_max"],
        })

    # --- Validator delinquency absolute threshold ---
    delinquency_now = validators.get("delinquency_pct")
    if delinquency_now is not None and delinquency_now >= thresholds["validator_delinquency_pct_max"]:
        anomalies.append({
            "metric": "delinquency_pct",
            "severity": "critical" if delinquency_now >= 2 * thresholds["validator_delinquency_pct_max"] else "warning",
            "message": f"Validator delinquency at {delinquency_now}% (>= {thresholds['validator_delinquency_pct_max']}% threshold).",
            "value": delinquency_now,
            "threshold": thresholds["validator_delinquency_pct_max"],
        })

    # --- TVL 24h change ---
    tvl_change = econ.get("solana_tvl_change_24h_pct")
    if tvl_change is not None and abs(tvl_change) >= thresholds["tvl_change_pct_24h"]:
        direction = "surge" if tvl_change > 0 else "drawdown"
        anomalies.append({
            "metric": "solana_tvl_change_24h_pct",
            "severity": "warning",
            "message": f"TVL {direction} of {tvl_change}% in 24h (>= {thresholds['tvl_change_pct_24h']}% threshold).",
            "value": tvl_change,
            "threshold": thresholds["tvl_change_pct_24h"],
        })

    # --- SOL price 24h change ---
    price_change = econ.get("sol_price_change_24h_pct")
    if price_change is not None and abs(price_change) >= thresholds["sol_price_change_pct_24h"]:
        direction = "up" if price_change > 0 else "down"
        anomalies.append({
            "metric": "sol_price_change_24h_pct",
            "severity": "info",
            "message": f"SOL price {direction} {abs(price_change)}% in 24h (>= {thresholds['sol_price_change_pct_24h']}% threshold).",
            "value": price_change,
            "threshold": thresholds["sol_price_change_pct_24h"],
        })

    return anomalies
