# Object-Store Landing and External Table

[Faiz Elahi](https://www.linkedin.com/in/faizilahi) — [pendataco.com](https://pendataco.com) — [github.com/faizilahi](https://github.com/faizilahi)

Synthetic data only. No vendor-customer employment claim.

OCI Object Storage-style landing (`raw/y=2024/m=09/d=15/`) with an external
table definition over CSV. Count mismatch taught: missing `_SUCCESS` marker
caused the external table to read a partial prefix.

## The bucket layout

`bucket/raw/y=2024/m=09/d=15/part-*.csv` — **8** parts, **20,000** rows when complete.

## The external table

`sql/ext_orders.sql` — `ORACLE_BIGDATA` style external table simulation.

## The count

Without `_SUCCESS`, reader saw **5/8** files → **12,500** rows. With marker,
**20,000** rows.

```powershell
pip install -r requirements.txt
python scripts/generate_synthetic_data.py
python src/run_external.py
```
