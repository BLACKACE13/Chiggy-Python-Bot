from database import connection as con
import os.path
import json

async def check_balance(uid):
    """
    Returns the balance of the user from their user id.
    """
    prefetcher_file = os.path.join(os.path.dirname(__file__), "./prefetch_data/cash_cache.json")
    with open(prefetcher_file) as f:
        data = json.load(f)
    return(data.get(str(uid)))


async def add_balance(uid, amount):
    """
    Adds the given amount to the respected user.
    """
    prefetcher_file = os.path.join(os.path.dirname(__file__), "./prefetch_data/cash_cache.json")

    with open(prefetcher_file) as f:
            cash_data = json.load(f)
    if str(uid) in cash_data:
        cash_data[str(uid)] = cash_data[str(uid)] + amount
    else:
        cash_data[str(uid)] = 20000 + amount

    with open(prefetcher_file, "w") as f:
        json.dump(cash_data, f, indent=4)


async def remove_balance(uid, amount):
    """
    Removes the given amount from the respected user.
    """
    prefetcher_file = os.path.join(os.path.dirname(__file__), "./prefetch_data/cash_cache.json")

    with open(prefetcher_file) as f:
            cash_data = json.load(f)

    if str(uid) in cash_data:
        cash_data[str(uid)] = cash_data[str(uid)] - amount
    else:
        cash_data[str(uid)] = 20000 - amount

    with open(prefetcher_file, "w") as f:
        json.dump(cash_data, f, indent=4)

async def cash_prefetcher():
    """
    Prefetches the data from the database and stores in the json file.
    """

    prefetched_cash_data = {}
    prefetcher_cash_file = os.path.join(os.path.dirname(__file__), "./prefetch_data/cash_cache.json")
    db = con.create_conn()
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM CASH')
    result = cursor.fetchall()
    for i in result:
        prefetched_cash_data[i[0]] = i[1]
    with open(prefetcher_cash_file, "w") as f:
            json.dump(prefetched_cash_data, f, indent=4)

async def cash_postsyncer(uid_list):
    """
    Syncs the data from the json file to the database.
    """
    postsyncer_cash_file = os.path.join(os.path.dirname(__file__), "./prefetch_data/cash_cache.json")
    with open(postsyncer_cash_file) as f:
        data = json.load(f)
    db = con.create_conn()
    cursor = db.cursor()
    for uid in uid_list:
        cursor.execute(f'UPDATE CASH SET CASH = {data.get(str(uid))} WHERE id = "{uid}"')
   
async def inventory_prefetcher():
    """
    Prefetches the data from the database and stores in the json file.
    """
    prefetched_inventory_data = {}
    prefetcher_inventory_file = os.path.join(os.path.dirname(__file__), "./prefetch_data/inventory_cache.json")
    db = con.create_conn()
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM INVENTORY')
    result = cursor.fetchall()
    for i in result:
        prefetched_inventory_data[i[0]] = {
            "tea" : i[1] ,
            "coffee" : i[2],
            "cookie" : i[3],
            "dog" : i[4],
            "phone" : i[5],
            "smartwatch": i[6],
            "rose": i[7]
            }
    with open(prefetcher_inventory_file, "w") as f:
            json.dump(prefetched_inventory_data, f, indent=4)

async def inventory_postsyncer(uid_list):
    """
    Syncs the data from the json file to the database.
    """
    postsyncer_inventory_file = os.path.join(os.path.dirname(__file__), "./prefetch_data/inventory_cache.json")
    with open(postsyncer_inventory_file) as f:
        data = json.load(f)
    db = con.create_conn()
    cursor = db.cursor()
    for uid in uid_list:
        cursor.execute(f'''UPDATE INVENTORY SET
        tea = {data[(uid)]["tea"]},
        coffee =  {data[uid]["coffee"]},
        cookie = {data[uid]["cookie"]},
        dog = {data[uid]["dog"]},
        phone = {data[uid]["phone"]},
        smartwatch = {data[uid]["smartwatch"]},
        rose = {data[uid]["rose"]} WHERE id = "{uid}"''')


async def add_item(uid, item ,amount):
    """
    Adds the item to their inventory data.
    """
    prefetcher_file = os.path.join(os.path.dirname(__file__), "./prefetch_data/inventory_cache.json")

    with open(prefetcher_file) as f:
        inventory_data = json.load(f)
    if str(uid) in inventory_data:
        inventory_data[str(uid)][item] = inventory_data[str(uid)][item] + amount
    else:
        inventory_data[str(uid)][item] = amount

    with open(prefetcher_file, "w") as f:
        json.dump(inventory_data, f, indent=4)


async def remove_item(uid,item, amount):
    """
    Removes the item to their inventory data.
    """
    prefetcher_file = os.path.join(os.path.dirname(__file__), "./prefetch_data/inventory_cache.json")

    with open(prefetcher_file) as f:
            inventory_data = json.load(f)
    if str(uid) in inventory_data:
        inventory_data[str(uid)][item] = inventory_data[str(uid)][item] - amount
    else:
        inventory_data[str(uid)][item] = amount

    with open(prefetcher_file, "w") as f:
        json.dump(inventory_data, f, indent=4)