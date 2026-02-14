from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


class AuditLogger:
    def __init__(self, path: str = "logs/signal_audit.log") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def log(self, payload: dict) -> None:
        record = {"ts": datetime.utcnow().isoformat(), **payload}
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")
