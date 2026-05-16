"""Training loop scaffold for CQL experiments."""

from pathlib import Path
from typing import Dict, List

from config import settings
from core.data_loader import load_medical_data
from core.model import CQLModel
from core.preprocessor import preprocess_batch
from utils.logger import log_info


class Trainer:
    def __init__(self) -> None:
        self.model = CQLModel(
            name=settings.MODEL_NAME,
            learning_rate=settings.LEARNING_RATE,
        )

    def run(self, data_path: Path) -> Dict[str, float]:
        raw = load_medical_data(str(data_path))
        records: List[Dict] = raw.get("data", [])
        if not records:
            records = [{"patient_id": i, "value": i * 0.1} for i in range(64)]

        batch = preprocess_batch(records[: settings.BATCH_SIZE])
        metrics = {"loss": 0.0}

        for epoch in range(settings.NUM_EPOCHS):
            metrics = self.model.train_step(batch)
            log_info(f"epoch={epoch + 1} loss={metrics['loss']:.4f}")

        settings.RESULT_DIR.mkdir(parents=True, exist_ok=True)
        out_file = settings.RESULT_DIR / "metrics.txt"
        out_file.write_text(f"final_loss={metrics['loss']:.6f}\n", encoding="utf-8")
        log_info(f"saved metrics to {out_file}")
        return metrics
