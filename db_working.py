import sqlite3


def delete_offer(number):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    offer = list(filter(lambda s: s[0] == number, load_offers()))[0]
    cur.execute(f'DROP TABLE {offer[2]+str(number)}')
    cur.execute(f'DROP TABLE {offer[2]+str(number)}_sale')
    cur.execute('DELETE FROM offers WHERE number = ?', (number, ))
    k = load_workers()
    for i in k:
        cur.execute(f'delete from {i[1]} where offer_number = ?', (number, ))
    conn.commit()
    conn.close()



def delete_group(delete_name):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM service_grops WHERE name = ?', (delete_name, ))
    cur.execute('UPDATE services set grop = ? where grop = ?', ('Все', delete_name))
    conn.commit()
    conn.close()


def add_group(name):
    conn = sqlite3.connect('orders.db')
    need = (name, )
    conn.execute(
        f"""INSERT INTO service_grops (name) VALUES(?);""",
        need)
    conn.commit()
    conn.close()


def load_groups():
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM service_grops;")
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s


def load_pass():
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data;")
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s


def save_pass(passw):
    conn = sqlite3.connect('orders.db')
    conn.execute(
        f"""INSERT INTO data VALUES(?);""",
        (passw, ))
    conn.commit()
    conn.close()


def save_worker(name, works='', prices='', clients='', dates='', procents='', zp='', procent='', stat=1):
    conn = sqlite3.connect('orders.db')
    need = (name, procent, stat)
    conn.execute(
        f"""INSERT INTO workers (name, procent, sost) VALUES(?, ?, ?);""",
        need)
    conn.execute(f'''CREATE TABLE {name}(
    offer_number TEXT,
     price TEXT,
     work_name TEXT,
      date TEXT, 
      proc INTEGER);''')
    conn.commit()
    conn.close()


def fire(name, stat):
    conn = sqlite3.connect('orders.db')
    need = (stat, name)
    conn.execute(
        f"""UPDATE workers set sost = ? WHERE name = ?;""",
        need)
    conn.commit()
    conn.close()


def load_last():
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM sqlite_sequence where name = ?;", ('offers', ))
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s[0]


def save_offer(worker='', name='', client='', price='', service='', date='', procent='', phone='', number=''):
    try:
        s = [int(load_last()[1])]
    except:
        s = [0]
    number = s[0]
    conn = sqlite3.connect('orders.db')
    need = (worker, name, client, price, service, date, phone, 'nw')
    conn.execute(
        f"""INSERT INTO offers (type, name, client, price, services, date, phone, sost) VALUES(?, ?, ?, ?, ?, ?, ?, ?);""",
        need)
    conn.execute(f'''CREATE TABLE {name + str(number + 1)}(
        offer_number TEXT,
         work_name TEXT,
         price TEXT,
          col TEXT,
          date TEXT,
          worker TEXT,
          sost INTEGER,
          comm TEXT);''')
    conn.execute(f'''CREATE TABLE {name + str(number + 1)}_sale(
            offer_number TEXT,
             sale_name TEXT,
             price TEXT,
              col TEXT,
              date TEXT);''')
    conn.commit()
    conn.close()


def save_service(name, price, price2, group, procent=0):
    conn = sqlite3.connect('orders.db')
    need = (name, price, procent, price2, group)
    conn.execute(
        f"""INSERT INTO services (name, price, procent, price2, grop) VALUES(?, ?, ?, ?, ?);""",
        need)
    conn.commit()
    conn.close()


def save_sale(name, price, col, procent=0):
    conn = sqlite3.connect('orders.db')
    need = (name, col, price)
    conn.execute(
        f"""INSERT INTO in_sale (name, col, base_price) VALUES(?, ?, ?);""",
        need)
    conn.commit()
    conn.close()


def save_rash(name, col, price, date):
    conn = sqlite3.connect('orders.db')
    need = (name, col, price, date)
    conn.execute(
        f"""INSERT INTO ras (name, col, price, date) VALUES(?, ?, ?, ?);""",
        need)
    conn.commit()
    conn.close()


def load_workers():
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM workers;")
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s


def load_ras():
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ras;")
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s


def load_offers():
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM offers;")
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s


def load_services(grop=''):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM services;")
    s = cur.fetchall()
    cur.close()
    conn.close()
    if grop == '':
        return s
    else:
        k = []
        for i in s:
            if i[5] == grop:
                k.append(i)
        return k


def update_ras(number, col, price, name):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("""UPDATE ras set name = ? where number = ?""", (name, number))
    cur.execute("""UPDATE ras set price = ? where number = ?""", (price, number))
    cur.execute("""UPDATE ras set col = ? where number = ?""", (col, number))
    conn.commit()
    conn.close()


def delete_ras(number):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM ras where number = ?""", (number, ))
    conn.commit()
    conn.close()


def delete_service(number):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM services where number = ?""", (number,))
    conn.commit()
    conn.close()


def update_services(number, name, price,  price2, group):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    old_name = list(filter(lambda s: str(s[0]) == str(number), load_services()))[0][1]
    cur.execute("""UPDATE services set name = ? where number = ?""", (name, number))
    cur.execute("""UPDATE services set price = ? where number = ?""", (price, number))
    cur.execute("""UPDATE services set price2 = ? where number = ?""", (price2, number))
    cur.execute("""UPDATE services set grop = ? where number = ?""", (group, number))
    conn.commit()
    conn.close()
    offers = load_offers()
    for i in offers:
        conn = sqlite3.connect('orders.db')
        conn.execute(f'''UPDATE {(i[2]) + str(i[0])} set work_name = ? WHERE work_name = ?''', (name, old_name))
        conn.commit()
        conn.close()
    workers = load_workers()
    for i in workers:
        conn = sqlite3.connect('orders.db')
        conn.execute(f'''UPDATE {i[1]} set work_name = ? WHERE work_name = ?''', (name, old_name))
        conn.commit()
        conn.close()


def update_sale_1(number, name, price,  col):
    number = str(number)
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    old_name = list(filter(lambda s: str(s[0]) == str(number),load_in()))[0][1]
    cur.execute("""UPDATE in_sale set name = ? where number = ?""", (name, number,))
    cur.execute("""UPDATE in_sale set col = ? where number = ?""", (col, number,))
    cur.execute("""UPDATE in_sale set base_price = ? where number = ?""", (price, number,))
    conn.commit()
    conn.close()
    offers = load_offers()
    for i in offers:
        conn = sqlite3.connect('orders.db')
        conn.execute(f'''UPDATE {(i[2]) + str(i[0])}_sale set sale_name = ? WHERE sale_name = ?''', (name, old_name))
        conn.commit()
        conn.close()


def update_rec(number, rec, dop):
    conn = sqlite3.connect('orders.db')
    conn.execute(f'''UPDATE offers set services=?, price=? where number=?;''', (rec, dop, number,))
    conn.commit()
    conn.close()


def update_offer_data(number, client, phone, type):
    conn = sqlite3.connect('orders.db')
    conn.execute(f'''UPDATE offers set client=?, phone=?, type = ? where number=?;''', (client, phone, type, number,))
    conn.commit()
    conn.close()


def update_offer(number, work='', price='', worker='', dates='', col='', sost=0, comm=''):
    s = load_offers()
    name = ''
    for i in s:
        if str(i[0]) == str(number):
            name = i[2]
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    services = cur.execute(f'''SELECT * FROM {str(name) + str(number)};''').fetchall()
    ss = 0
    for i in services:
        if i[1] == work:
            ss = 1
    if ss:
        cur.execute(f"""UPDATE {str(name).strip() + str(number).strip()} set price = ?, col = ?, worker = ?, sost = ?, comm = ? where work_name = ?;""", (price, col, worker, sost, comm, work))
    else:
        cur.execute(f"""INSERT INTO {str(name) + str(number)} (offer_number, work_name, price, col, date, worker, sost, comm) VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", (number, work, price, col, dates, worker, sost, comm))
    conn.commit()
    conn.close()


def update_offer_sale(number, work='', price='', dates='', col=''):
    s = load_offers()
    name = ''
    for i in s:
        if str(i[0]) == str(number):
            name = i[2]
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    services = cur.execute(f'''SELECT * FROM {str(name) + str(number)}_sale;''').fetchall()
    num = 0
    b = 0
    inn = load_in()
    for i in inn:
        if i[1] == work:
            b = int(i[2])
            num = i[0]
            break
    ss = 0
    r = 0
    for i in services:
        if i[1] == work:
            ss = 1
            r = int(i[3])
            break
    if ss:
        r = int(col) - r
        b -= r
        update_in(num, b)
        cur.execute(f"""UPDATE {str(name).strip() + str(number).strip()}_sale set price = ?, col = ? where sale_name = ?;""", (price, col, work))
    else:
        update_in(num, b - int(col))
        cur.execute(f"""INSERT INTO {str(name) + str(number)}_sale (offer_number, sale_name, price, col, date) VALUES(?, ?, ?, ?, ?);""", (number, work, price, col, dates))
    conn.commit()
    conn.close()


def delete_from_worker(name, works='', number=''):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute(f"""DELETE FROM {str(name)} where offer_number = ? and work_name = ?""", (number, works))
    conn.commit()
    conn.close()


def update_procent(name, procent):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute('''UPDATE workers set procent = ? where name = ?''', (procent, name))
    conn.commit()
    conn.close()


def update_worker(name, works='', prices='', dates='', number=''):
    conn = sqlite3.connect('orders.db')
    need = (number, prices, works, dates)
    cur = conn.cursor()
    proc = int(list(filter(lambda s: s[1] == name, load_workers()))[0][2])
    ss = 0
    s = load_worker_service(name)
    for i in s:
        if str(i[0]) == str(number) and works == i[2]:
            ss = 1
    if ss:
        cur.execute(f"""UPDATE {str(name)} set price = ?, proc = ? where work_name = ? and offer_number = ?;""",
                    (prices, proc, works, str(number)))
    else:
        cur.execute(f"""INSERT INTO {name} (offer_number, price, work_name, date, proc) VALUES(?, ?, ?, ?, ?);""", (number, prices, works, dates, proc))
    conn.commit()
    conn.close()


def load_worker_service(name):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM {name};""")
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s


def load_in():
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM in_sale;""")
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s


def load_services1(number):
    s = load_offers()
    name = ''
    for i in s:
        if str(i[0]) == str(number[0]):
            name = i[2]
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM {name + str(number[0])};""")
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s


def load_sales(number):
    s = load_offers()
    name = ''
    for i in s:
        if str(i[0]) == str(number[0]):
            name = i[2]
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM {name + str(number[0])}_sale;""")
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s

def update_in(num, col):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute(f"""UPDATE in_sale set col = ? where number = ?;""", (col, num))
    cur.close()
    conn.commit()
    conn.close()


def update_sost(number, sost, date=''):
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    if date == '':
        cur.execute(f"""UPDATE offers set sost = ? where number = ?;""", (sost, number))
    else:
        cur.execute(f"""UPDATE offers set sost = ?, date_closed = ? where number = ?;""", (sost, date, number))
    cur.close()
    conn.commit()
    conn.close()
