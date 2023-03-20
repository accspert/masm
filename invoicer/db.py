import sqlite3

conn = sqlite3.connect("../db.sqlite3")
cur = conn.cursor()

def get_entrys(date):
    cur.execute("""
    select 
    Amount, Firstname, Lastname, Street, Housenummer, Citycode, City, IBAN, Email
    from Dueto
    inner join People on People.ID = Dueto.Personid
    inner join Bankdata on Bankdata.Personid  = Dueto.Personid
    inner join Person_Address_Match on Person_Address_Match.Personid = Dueto.Personid
    inner join Addresses on Addresses.ID = Person_Address_Match.Addressid
    where Duedate = (?) OR
    Duedate = 'test'
    """, (date,))
    return cur.fetchall()

def delete_entrys(date):
    cur.execute("""
    delete from Dueto where Duedate = (?)
    """, (date,))
    return True

def close():
    conn.commit()
    conn.close()