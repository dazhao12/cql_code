"""A tiny placeholder CQL model interface."""

from typing import Dict, List


class CQLModel:
    def __init__(self, name: str, learning_rate: float) -> None:
        self.name = name
        self.learning_rate = learning_rate

    def train_step(self, batch: List[Dict]) -> Dict[str, float]:
        # Mock loss value for scaffold demonstration.
        loss = max(0.01, 1.0 / (len(batch) + 1))
        return {"loss": loss}
