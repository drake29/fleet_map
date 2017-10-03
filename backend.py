import requests
import sqlite3

def connect():
	conn=sqlite3.connect("vessel_db.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS fleet (id INTEGER PRIMARY KEY, Vessel TEXT, MMSI NUMERIC)")
	conn.commit()
	conn.close()

def insert(Vessel,MMSI):
	conn=sqlite3.connect("vessel_db.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO fleet VALUES (NULL,?,?)",(Vessel,MMSI))
    #NULL b/c the primary key auto-increments, so dont need to give the key additional values as we go.
	conn.commit()
	conn.close()

#Fetch all the rows of the table:
def view_all():
	conn=sqlite3.connect("Vessel_db.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM fleet")
	#Dont neeed a commit method when fetching/viewing, only for writing
	rows=cur.fetchall()
	conn.close()
	return rows

def update(id, Vessel, MMSI):
	conn=sqlite3.connect("Vessel_db.db")
	cur=conn.cursor()
	cur.execute("UPDATE fleet SET Vessel=?, MMSI=? WHERE id=?", (Vessel, MMSI,id))
	conn.commit()
	conn.close()

def get_mmsi():
	conn=sqlite3.connect("Vessel_db.db")
	cur=conn.cursor()
	cur.execute("SELECT MMSI FROM fleet;")
	rows=cur.fetchall()
	conn.close()
	rows = [str(i[0]) for i in rows]##fetchall() returns a list of tuples, use list comprehension to convert to a list of strings
	return rows
	
connect()
#insert("Bulk Juliana", 352486000)
# insert("Bulk Trident", 371600000)
# insert("Bulk Beothuk", 355236000)
# insert("Bulk Destiny", 352244000)
# insert("Bulk Power", 356675000)
# insert("Bulk Progress", 355641000)
# insert("Bulk Endurance", 356515000)

#print (get_mmsi())
#print (view_all())

