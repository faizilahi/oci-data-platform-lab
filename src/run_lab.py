"""Bronze object files + warehouse-style SQL."""
from pathlib import Path
import shutil
import duckdb

ROOT = Path(__file__).resolve().parents[1]
BRONZE = ROOT / "data" / "object_storage" / "bronze"
BRONZE.mkdir(parents=True, exist_ok=True)
for name in ("hcm_employees.csv", "ebs_gl_journals.csv"):
    shutil.copy(ROOT / "data" / name, BRONZE / name)

con = duckdb.connect()
print(con.execute("""
SELECT job_code, COUNT(*) AS headcount, AVG(salary_usd) AS avg_salary
FROM read_csv_auto(?)
GROUP BY 1 ORDER BY headcount DESC
""", [str(BRONZE / "hcm_employees.csv")]).fetchdf())
print(con.execute("""
SELECT ledger, SUM(debit) AS total_debit, SUM(credit) AS total_credit
FROM read_csv_auto(?)
GROUP BY 1
""", [str(BRONZE / "ebs_gl_journals.csv")]).fetchdf())
