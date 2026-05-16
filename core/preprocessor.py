"""Simple data preprocessing utilities."""

from typing import Dict, List


def preprocess_batch(records: List[Dict]) -> List[Dict]:
    """Mock preprocess step: keep schema and mark normalized."""
    cleaned = []
    for row in records:
        new_row = dict(row)
        new_row["normalized"] = True
        cleaned.append(new_row)
    return cleaned
