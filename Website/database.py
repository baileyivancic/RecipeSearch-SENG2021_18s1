import os
import sqlite3

class Database(object):
	def __init__(self):
		pass

	def first_run(self):
		db = sqlite3.connect('database.db')
		cursor = db.cursor()

		#create table for authenticated users
		cursor.execute('''CREATE TABLE IF NOT EXISTS
                		  	loginDetails(userID 		INT  PRIMARY KEY  NOT NULL,
					  					 username 		TEXT,
							 		 	 password		TEXT)''')

		#create table for saved recipes
		#recipeIngredients - comma separated string of recipeIngredients?
		#cursor.execute('''CREATE TABLE IF NOT EXISTS
		 #			  	  	savedRecipes(recipeID			INT		PRIMARY KEY NOT NULL,
		#								 userID				INT 	FOREIGN KEY NOT NULL,
		#								 recipename			TEXT,
		#								 recipeIngredients	TEXT )''')


		#cursor.execute('''CREATE TABLE IF NOT EXISTS
		 #			  	  	savedIngredients(ingredientID	INT		PRIMARY KEY NOT NULL,
		#									 userID 		INT 	FOREIGN KEY NOT NULL,
		#								 	 ingredient		TEXT )''')

		db.commit()
		db.close()




	def register_user(self, username, password):
		db = sqlite3.connect('database.db')
		cursor = db.cursor()

		cursor.execute("SELECT EXISTS(SELECT 1 FROM loginDetails WHERE username=? AND password=?)", (username, password))
		temp =  cursor.fetchone()

		print("result from db ", temp)
		if temp != (0, ):
			# there is already a user using this user name
			db.commit()
			db.close()
			return 0
		else :
			cursor.execute('''SELECT MAX(userID) FROM loginDetails''')
			i = cursor.fetchone()
			if i[0]!=None:
				x = i[0] + 1
			else:
				x = 1
			cursor.execute('''INSERT INTO loginDetails (userID, username, password) VALUES (?,?,?)''',(x, username, password))
			db.commit()
			db.close()
			return 1


	def isValidUser(self, username, password):
		db = sqlite3.connect('database.db')
		cursor = db.cursor()

		cursor.execute("SELECT EXISTS(SELECT 1 FROM loginDetails WHERE username=? AND password=?)", (username, password, ))
		temp =  cursor.fetchone()

		isValid = False

		if temp != (0, ):
			# there is already a user using this user name
			isValid = True


		db.commit()
		db.close()
		return isValid

	def getSavedIng(self,userID):
		print(userID)
		db = sqlite3.connect('database.db')
		cursor = db.cursor()
		cursor.execute("SELECT userID FROM loginDetails WHERE username=(?)",(userID,))
		ID = cursor.fetchone()
		cursor.execute("SELECT ingredient FROM savedingredient WHERE userID=(?)",(ID[0],))
		tmp = list(cursor.fetchall())
		new = list()
		for i in tmp:
			i = str(i)
			i = i.strip(',)')
			i = i.strip("'")
			i = i.strip("('")
			new.append(i)

		db.commit()
		db.close()
		return new

	def addIng(self,ing,userID):
		db = sqlite3.connect('database.db')
		cursor = db.cursor()
		cursor.execute("SELECT userID FROM loginDetails WHERE username=(?)",(userID,))
		ID = cursor.fetchone()
		cursor.execute('''INSERT INTO savedingredient (userID,ingredient) VALUES (?,?)''',(ID[0],ing))
		db.commit()
		db.close()

	def delIng(self,ing,userID):
		db = sqlite3.connect('database.db')
		cursor = db.cursor()
		cursor.execute("SELECT userID FROM loginDetails WHERE username=(?)",(userID,))
		ID = cursor.fetchone()
		cursor.execute('''DELETE FROM savedingredient WHERE userID=(?) AND ingredient=(?)''',(ID[0],ing))
		db.commit()
		db.close()

	def saveRecipe(self,rec,userID):
		db = sqlite3.connect('database.db')
		cursor = db.cursor()
		cursor.execute("SELECT userID FROM loginDetails WHERE username=(?)",(userID,))
		ID = cursor.fetchone()
		cursor.execute('''INSERT INTO savedrecipe (userID,recipe) VALUES (?,?)''',(ID[0],rec))
		db.commit()
		db.close()

	def getSavedRecipes(self,userID):
		print(userID)
		db = sqlite3.connect('database.db')
		cursor = db.cursor()
		cursor.execute("SELECT userID FROM loginDetails WHERE username=(?)",(userID,))
		ID = cursor.fetchone()
		cursor.execute("SELECT recipe FROM savedrecipe WHERE userID=(?)",(ID[0],))
		new = list()

		for i in cursor.fetchall():
			new.append(i[0])

		db.commit()
		db.close()
		return new
	
	def delRecipe(self,recipe,userID):
		db = sqlite3.connect('database.db')
		cursor = db.cursor()
		cursor.execute("SELECT userID FROM loginDetails WHERE username=(?)",(userID,))
		ID = cursor.fetchone()
		cursor.execute('''DELETE FROM savedrecipe WHERE userID=(?) AND recipe=(?)''',(ID[0],recipe))
		db.commit()
		db.close()

