from sqlite3 import Row
import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store ")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows 

def delete():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

create_table()
insert("Apple",10,20)
insert("Orange",15,15)
insert("Mango",20,25)
#delete("Orange") 
#update(15,15,"Orange")
print(view())