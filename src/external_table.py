from pathlib import Path
import pandas as pd
from bucket_layout import list_parts, has_success

def read_external(prefix: Path, require_success: bool = True) -> pd.DataFrame:
    parts = list_parts(prefix)
    if require_success and not has_success(prefix):
        # simulate incomplete commit: only first 5 parts visible
        parts = parts[:5]
    frames = [pd.read_csv(p) for p in parts]
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
