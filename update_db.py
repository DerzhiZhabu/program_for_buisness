from db_working import *
s = load_offers()
'''conn = sqlite3.connect('orders.db')
cur = conn.cursor()
for i in s:
    cur.execute(f"""ALTER TABLE {str(i[2]) + str(i[0])} ADD COLUMN sost INTEGER;""")
conn.commit()
conn.close()'''
'''conn = sqlite3.connect('orders.db')
cur = conn.cursor()
for i in s:
    if i[7] == 'cor':
        cur.execute(f"""UPDATE {str(i[2]) + str(i[0])} set sost = ?;""", (1,))
    else:
        cur.execute(f"""UPDATE {str(i[2]) + str(i[0])} set sost = ?;""", (0, ))
conn.commit()
conn.close()'''
'''conn = sqlite3.connect('orders.db')
cur = conn.cursor()
s = load_workers()
print(s)
for i in s:
    cur.execute(f"""ALTER TABLE {i[1]} ADD COLUMN proc INTEGER;""")
conn.commit()
conn.close()'''
'''conn = sqlite3.connect('orders.db')
cur = conn.cursor()
s = load_workers()
print(s)
for i in s:
    cur.execute(f"""UPDATE {i[1]} set proc = ?;""", (int(i[-1]), ))
conn.commit()
conn.close()'''