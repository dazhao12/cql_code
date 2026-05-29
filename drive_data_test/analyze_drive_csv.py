#!/usr/bin/env python3
import csv
import statistics
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python analyze_drive_csv.py <csv_path>")
        return 2

    csv_path = Path(sys.argv[1])
    rows = list(csv.DictReader(csv_path.open(newline="")))
    co2_values = [float(row["co2"]) for row in rows]
    rso2_values = [float(row["rso2"]) for row in rows]

    print(f"rows={len(rows)}")
    print(f"co2_mean={statistics.mean(co2_values):.2f}")
    print(f"rso2_mean={statistics.mean(rso2_values):.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
