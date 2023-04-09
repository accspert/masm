import pymysql
import sqlite3

conn = pymysql.connect(host="127.0.0.1",
                       port=3306,
                       user="masm",
                       passwd="46uR81KepdO7NXq7ZFu2d",
                       db="masm",
                       cursorclass=pymysql.cursors.DictCursor)

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
    where Duedate = (%s) OR
    Duedate = 'test'
    """, date)
    return cur.fetchall()

def delete_entrys(date):
    cur.execute("""
    delete from Dueto where Duedate = (%s)
    """, date)
    conn.commit()
    return True

def close():
    conn.commit()
    conn.close()
