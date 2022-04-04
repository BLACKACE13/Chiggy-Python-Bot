from database import connection as con
import os.path
import json

async def user_check_cash(uid):
    """
    Checks for a user in the database and if it does not exists adds it in the database.
    """
    cash_cache_file = os.path.join(os.path.dirname(__file__), "./prefetch_data/cash_cache.json")
    with open(cash_cache_file) as f:
        cash_data = json.load(f)
    if str(uid) not in cash_data:
        db = con.create_conn()
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO CASH(id) VALUES({uid})")
        cash_data[str(uid)] = 20000
        with open(cash_cache_file, "w") as f:
            json.dump(cash_data, f, indent=4)

async def user_check_inventory(uid):
    """
    Checks for a user in the database and if it does not exists adds it in the database.
    """
    inventory_cache_file = os.path.join(os.path.dirname(__file__), "./prefetch_data/inventory_cache.json")

    with open(inventory_cache_file) as f:
        inventory_data = json.load(f)
    
    if str(uid) not in inventory_data:
     
        db = con.create_conn()
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO INVENTORY VALUES({uid} , 0 ,0,0,0,0,0,0)") 
        inventory_data[str(uid)] = {
        "tea": 0,
        "coffee": 0,
        "cookie": 0,
        "dog": 0,
        "phone": 0,
        "smartwatch": 0,
        "rose": 0
    }
        with open(inventory_cache_file, "w") as f:
            json.dump(inventory_data, f, indent=4)



async def table_check():
    """
    Checks if the tables are available in the database if not creates.
    """
    db = con.create_conn()
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS CASH
    (id VARCHAR(255),
    cash BIGINT DEFAULT 20000)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS INVENTORY
    (id VARCHAR(255),
    tea BIGINT,
    coffee BIGINT,
    cookie BIGINT,
    dog BIGINT,
    phone BIGINT,
    smartwatch BIGINT,
    rose BIGINT)""")