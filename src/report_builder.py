"""
Orchestrates a single end-to-end report generation cycle:
fetch -> derive metrics -> detect anomalies -> render JSON/MD/HTML -> persist history.
"""
import datetime
import json
import os

from . import config
from . import rpc_client
from . import external_sources
from . import metrics
from . import anomaly_detector
from . import history_store
from . import markdown_report
from . import dashboard


def build_report() -> dict:
    onchain = rpc_client.collect_onchain_snapshot()
    offchain = external_sources.collect_offchain_snapshot()

    perf = metrics.network_performance(onchain)
    validators = metrics.validator_status(onchain)
    sol_price_usd = ((offchain.get("sol_price") or {}).get("solana", {}) or {}).get("usd")
    fee_estimate = metrics.fee_and_rev_estimate(onchain, sol_price_usd)
    econ = metrics.economic_indicators(offchain, fee_estimate)
    growth = metrics.ecosystem_growth(offchain)

    source_errors = {}
    source_errors.update(onchain.get("_errors", {}))
    source_errors.update(offchain.get("_errors", {}))

    report = {
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "network_performance": perf,
        "validator_status": validators,
        "economic_indicators": econ,
        "fee_and_rev_detail": fee_estimate,
        "ecosystem_growth": growth,
        "upcoming_developments": config.UPCOMING_DEVELOPMENTS,
        "source_errors": source_errors,
    }

    history = history_store.load_history()
    report["anomalies"] = anomaly_detector.detect_anomalies(report, history)

    return report, history


def write_outputs(report: dict, history: list) -> None:
    os.makedirs(config.DATA_DIR, exist_ok=True)
    os.makedirs(config.DOCS_DIR, exist_ok=True)

    with open(config.LATEST_JSON, "w") as f:
        json.dump(report, f, indent=2)

    with open(config.LATEST_MD, "w") as f:
        f.write(markdown_report.render_markdown(report))

    with open(config.DASHBOARD_HTML, "w") as f:
        f.write(dashboard.render_dashboard(report, history))

    history_store.append_snapshot(report)


def run_once(verbose: bool = True) -> dict:
    report, history = build_report()
    write_outputs(report, history)
    if verbose:
        n_errors = len(report.get("source_errors", {}))
        n_anomalies = len(report.get("anomalies", []))
        print(
            f"[{report['generated_at_utc']}] report generated — "
            f"{n_anomalies} anomaly(ies), {n_errors} source error(s). "
            f"Wrote {config.LATEST_JSON}, {config.LATEST_MD}, {config.DASHBOARD_HTML}"
        )
    return report
