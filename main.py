#!/usr/bin/env python3
"""
Solana Ecosystem Report — CLI entrypoint.

Usage:
    python main.py --once              Generate one report and exit (used by CI/cron).
    python main.py --loop               Generate reports forever, refreshing on an interval.
    python main.py --loop --interval 300   Same, but every 300 seconds instead of the default.

No API keys required. See README.md for full setup + methodology.
"""
import argparse
import sys
import time

from src import config
from src.report_builder import run_once


def main():
    parser = argparse.ArgumentParser(description="Solana Ecosystem Report generator")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--once", action="store_true", help="Generate a single report and exit.")
    mode.add_argument("--loop", action="store_true", help="Generate reports continuously on an interval.")
    parser.add_argument(
        "--interval", type=int, default=config.REFRESH_INTERVAL_SECONDS,
        help=f"Seconds between refreshes in --loop mode (default: {config.REFRESH_INTERVAL_SECONDS}).",
    )
    args = parser.parse_args()

    if args.once:
        run_once()
        return

    print(f"Starting continuous refresh every {args.interval}s. Press Ctrl+C to stop.")
    try:
        while True:
            try:
                run_once()
            except Exception as e:  # noqa: BLE001 - a single bad cycle should never kill the loop
                print(f"Report cycle failed, will retry next interval: {e}", file=sys.stderr)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
