"""
Tiny flat-file history store — one JSON snapshot per line, no database.
Kept deliberately simple (jsonl) so the whole pipeline still has zero
external dependencies and works fine committed straight into a git repo.
"""
import json
import os

from . import config


def load_history() -> list:
    if not os.path.exists(config.HISTORY_FILE):
        return []
    history = []
    with open(config.HISTORY_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    history.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return history


def append_snapshot(report: dict) -> None:
    os.makedirs(config.DATA_DIR, exist_ok=True)
    history = load_history()
    history.append(report)
    history = history[-config.HISTORY_MAX_SNAPSHOTS:]
    with open(config.HISTORY_FILE, "w") as f:
        for snap in history:
            f.write(json.dumps(snap) + "\n")
