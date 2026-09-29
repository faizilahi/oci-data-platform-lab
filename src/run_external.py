import json, sys
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from bucket_layout import list_parts, has_success
from external_table import read_external
PREFIX = ROOT / "bucket" / "raw" / "y=2024" / "m=09" / "d=15"
OUT = ROOT / "output"; OUT.mkdir(parents=True, exist_ok=True)

def main():
    partial = read_external(PREFIX, require_success=True)
    # write success and reread
    (PREFIX / "_SUCCESS").write_text("", encoding="utf-8")
    full = read_external(PREFIX, require_success=True)
    summary = {
        "parts": len(list_parts(PREFIX)),
        "partial_count": int(len(partial)),
        "full_count": int(len(full)),
        "had_success_after_fix": has_success(PREFIX),
    }
    full.to_csv(OUT / "ext_orders.csv", index=False)
    pd.DataFrame([summary]).to_csv(OUT / "count.csv", index=False)
    print(json.dumps(summary, indent=2))
if __name__ == "__main__":
    main()
