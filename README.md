# Quick ETL Demo

**Purpose**  
End‑to‑end demo that satisfies adroitts deliverables: high‑level design, ETL code, unit tests, runbook, and traceability matrix.

## Prerequisites
- Python 3.12+
- Homebrew Postgres 15 (or any local Postgres listening on `etl_demo`)

## Quick Start
```bash
python etl/load_sales.py     # load sample_sales.csv into Postgres
pytest -q                    # run tests
High‑Level Design
Extract sample_sales.csv
Transform via Pandas (type casting)
Load into Postgres table sales
Detailed Design
Table schema: order_id INT PK, order_date DATE, product TEXT, qty INT, price NUMERIC
Load mode: REPLACE (rerunnable demo)
See runbook.md for ops steps and RTM.csv for requirement mapping.

Save the file.

---

## 3  Runbook & RTM Touch‑Up

### runbook.md (minimal)

```md
## Daily Run
python etl/load_sales.py

## Failure Recovery
If the script errors, check Postgres is running (`brew services list`) and rerun.

## Table Reset
The script uses `if_exists="replace"` so reruns are idempotent.
ID,Requirement,Implementation
1,High‑level ETL design,README.md
2,Detailed ETL design,etl/load_sales.py comments
3,ETL code development,etl/load_sales.py
4,Unit tests,tests/test_load.py
5,Runbook,user guide,runbook.md
