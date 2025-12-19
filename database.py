import tinydb as tdb

DB_PATH = "data/db.json"
db = tdb.TinyDB(DB_PATH)

users_table   = db.table("users")
devices_table = db.table("devices")