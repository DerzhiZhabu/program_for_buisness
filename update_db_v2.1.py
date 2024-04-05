from db_working import *
conn = sqlite3.connect('orders.db')
offers = load_offers()
cur = conn.cursor()
for i in offers:
    cur.execute(f"ALTER TABLE {i[2] + str(i[0])} ADD COLUMN comm STRING;")
conn.commit()
conn.close()
