"""Very small logger helper for scripts."""

from datetime import datetime


def log_info(message: str) -> None:
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [INFO] {message}")
