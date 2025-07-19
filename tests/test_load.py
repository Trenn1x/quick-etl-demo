import subprocess, psycopg2, os, time

def test_etl_loads_rows():
    # Run ETL
    subprocess.run(["python", "etl/load_sales.py"], check=True)
    time.sleep(1)  # give db a sec
    conn = psycopg2.connect(dbname="etl_demo")

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM sales;")
    rows = cur.fetchone()[0]
    conn.close()
    assert rows >= 3
