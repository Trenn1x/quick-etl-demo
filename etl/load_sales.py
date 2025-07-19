import os
import pandas as pd
from sqlalchemy import create_engine, text

CSV_PATH = os.getenv("CSV_PATH", "sample_sales.csv")
DB_URL   = "postgresql:///etl_demo"   # local Homebrew Postgres

def load_csv_to_db():
    # 1. Extract
    df = pd.read_csv(CSV_PATH)

    # 2. Connect
    engine = create_engine(DB_URL)
    with engine.begin() as conn:
        # 3. Ensure table exists (DDL)
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS sales (
                order_id   INT PRIMARY KEY,
                order_date DATE,
                product    TEXT,
                qty        INT,
                price      NUMERIC
            );
        """))
        # 4. Load (replace so reruns don't error)
        df.to_sql("sales", conn, if_exists="replace", index=False)

if __name__ == "__main__":
    load_csv_to_db()
    print("✅ CSV loaded")
