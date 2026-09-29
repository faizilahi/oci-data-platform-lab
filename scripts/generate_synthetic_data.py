"""HCM/EBS-style synthetic HR and finance extracts."""
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(parents=True, exist_ok=True)

employees = pd.DataFrame({
    "person_number": [f"E{i:05d}" for i in range(1, 61)],
    "full_name": [f"Employee {i}" for i in range(1, 61)],
    "job_code": ["ANALYST", "NURSE", "ADMIN", "ENGINEER"] * 15,
    "hire_date": pd.date_range("2018-01-01", periods=60, freq="60D").strftime("%Y-%m-%d"),
    "salary_usd": [55000 + (i * 900) % 45000 for i in range(1, 61)],
})
employees.to_csv(DATA / "hcm_employees.csv", index=False)

gl = pd.DataFrame({
    "journal_id": [f"J{i:06d}" for i in range(1, 91)],
    "ledger": ["US_PRIMARY", "EU_PRIMARY"] * 45,
    "account": (["6000", "6100", "4000", "2100"] * 22 + ["6000", "6100"])[:90],
    "debit": [round(1000 + (i % 13) * 250, 2) for i in range(1, 91)],
    "credit": [0.0 if i % 2 else round(500 + (i % 7) * 100, 2) for i in range(1, 91)],
    "accounting_date": pd.date_range("2024-03-01", periods=90, freq="4D").strftime("%Y-%m-%d"),
})
gl.to_csv(DATA / "ebs_gl_journals.csv", index=False)
print("Wrote hcm_employees.csv and ebs_gl_journals.csv")
