"""Primary entry script for the CQL scaffold."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import settings
from core.trainer import Trainer


def main() -> None:
    trainer = Trainer()
    trainer.run(settings.DATA_PATH)


if __name__ == "__main__":
    main()
