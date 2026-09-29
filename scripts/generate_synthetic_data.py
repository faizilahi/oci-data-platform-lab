from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "bucket" / "raw" / "y=2024" / "m=09" / "d=15"
DATA.mkdir(parents=True, exist_ok=True)
for i in range(8):
    start = i * 2500
    pd.DataFrame({
        "order_id": [f"O{j:05d}" for j in range(start, start + 2500)],
        "amount": [10 + (j % 50) for j in range(start, start + 2500)],
        "order_date": "2024-09-15",
    }).to_csv(DATA / f"part-{i:05d}.csv", index=False)
# no _SUCCESS yet
print("parts written without _SUCCESS")
