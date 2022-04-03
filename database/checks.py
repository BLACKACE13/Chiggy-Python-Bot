from database import connection as con
import os.path
import json

async def user_check_cash(uid):
    prefetcher_file = os.path.join(os.path.dirname(__file__), "./prefetch_data/cash_cache.json")
    with open(prefetcher_file) as f:
        cash_data = json.load(f)
    if str(uid) not in cash_data:
        db = con.create_conn()
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO CASH(id) VALUES({uid})")
        cash_data[str(uid)] = 20000
        with open(prefetcher_file, "w") as f:
            json.dump(cash_data, f, indent=4)

async def user_check_inventory(uid):
    prefetcher_file = os.path.join(os.path.dirname(__file__), "./prefetch_data/inventory_cache.json")
    with open(prefetcher_file) as f:
        cash_data = json.load(f)
    if str(uid) not in cash_data:
        db = con.create_conn()
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO INVENTORY(id) VALUES({uid})")
        cash_data[str(uid)] = 20000
        with open(prefetcher_file, "w") as f:
            json.dump(cash_data, f, indent=4)

async def user_check(uid):
    await user_check_cash(uid)
    await user_check_inventory(uid)
    
async def table_check():
    db = con.create_conn()
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS CASH(id VARCHAR(255) , cash BIGINT DEFAULT 20000)")
    cursor.execute("CREATE TABLE IF NOT EXISTS INVENTORY(id VARCHAR(255) , tea BIGINT, coffee BIGINT,cookie BIGINT,dog BIGINT,phone BIGINT,smartwatch BIGINT,rose BIGINT)")