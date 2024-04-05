from db_working import *
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute(f"""ALTER TABLE services ADD COLUMN grop STRING;""")
cur.execute("CREATE TABLE service_grops (name	TEXT)")
cur.execute("UPDATE services set grop = ?", ('Все', ))
conn.commit()
conn.close()

