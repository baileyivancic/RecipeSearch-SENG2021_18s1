import os
import sqlite3

class Database(object):
	def __init__(self):
		pass

	def first_run(self):
		db = sqlite3.connect('database.db')
		cursor = db.cursor()


		cursor.execute('''CREATE TABLE IF NOT EXISTS
                loginDetails(userID 		INT  PRIMARY KEY  NOT NULL,
					  		 username 		TEXT,
							 password		TEXT)''')

		db.commit()
		db.close()

	def register_user(username, password):
		db = sqlite3.connect('database.db')
		cursor = db.cursor()

		cursor.execute("SELECT EXISTS(SELECT 1 FROM loginDetails WHERE username=?)", (username, ))
		temp =  cursor.fetchone

		isValid = True;

		if temp != (0, ):
			# there is already a user using this user name
			isValid = false;
		else :
			cursor.execute('''SELECT MAX(id) FROM loginDetails''')
			i = cursor.fetchone()
			if i[0]!=None:
				x = i[0] + 1
			else:
				x = 1
			cursor.execute('''INSERT INTO loginDetails (userID, username, password) VALUES (?,?,?)''',
							(x, username, password))

		db.commit()
		db.close()
		return isValid
