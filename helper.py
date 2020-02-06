import sqlite3
import random 

#for id's because users dont set them

DB_PATH = './todo.db'

# connect to database
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS "complete" ("id" TEXT NOT NULL, "task" TEXT NOT NULL, PRIMARY KEY("id"));""")
# save the change
c.execute("""CREATE TABLE IF NOT EXISTS "incomplete" ("id" TEXT NOT NULL, "task" TEXT NOT NULL, PRIMARY KEY("id"));""")
conn.commit()


def add_to_incomplete(task): 
	try:
		id = str(random.randrange(100,999))
		conn = sqlite3.connect(DB_PATH)
		c = conn.cursor()
		c.execute('insert into incomplete(id, task) values(?,?)', (id, task))
		conn.commit()
		return {"id": id}
		
	except Exception as e:
		print('Error: ', e)
		return None

def add_to_complete(inputId):
	try:
		conn = sqlite3.connect(DB_PATH)
		c = conn.cursor()
		c.execute('select task from incomplete where id=?', (inputId,))
		tasks = c.fetchone()[0]
		c.execute('insert into complete values(?,?)', (inputId,tasks))
		delete_task(inputId)
		conn.commit()
		return {"id": id}
		
	except Exception as e:
		print('Error: ', e)
		return None

def get_all_completes():
	try: 
		conn = sqlite3.connect(DB_PATH)
		c = conn.cursor()
		c.execute('select * from complete')
		rows = c.fetchall()
		conn.commit()
		return { "complete": rows }
	except Exception as e:
		print('Error: ', e)
		return None

def get_all_incompletes():
	try:
		conn = sqlite3.connect(DB_PATH)
		c = conn.cursor()
		c.execute('select * from incomplete')
		rows = c.fetchall()
		conn.commit()
		return { "incomplete": rows } 
	except Exception as e:
		print('Error: ', e)
		return None 

def uncomplete(inputId):
	try:
		conn = sqlite3.connect(DB_PATH)
		c = conn.cursor()
		c.execute('select task from complete where id=?', (inputId,))
		tasks = c.fetchone()[0]
		c.execute('insert into incomplete values(?,?)', (inputId,tasks))
		delete_task(inputId)
		conn.commit()
		return {"id": id}
		
	except Exception as e:
		print('Error: ', e)
		return None

def delete_task(inputId):
	try:
		conn = sqlite3.connect(DB_PATH)
		c = conn.cursor()
		c.execute('delete from complete where id=?', (inputId,))
		c.execute('delete from incomplete where id=?', (inputId,))
		conn.commit()
		return {"id":id}
	except Exception as e:
		print('Error: ', e)
		return None

def empty():
	try:
		conn = sqlite3.connect(DB_PATH)
		c = conn.cursor()
		c.execute('delete from complete')
		c.execute('delete from incomplete')
		conn.commit()
		return "you deleted everything mwahaha"
	except Exception as e:
		print('Error: ', e)
		return None

