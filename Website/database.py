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
		cursor.execute('''CREATE TABLE IF NOT EXISTS
		 			  	  	savedRecipes(recipeID			INT		PRIMARY KEY NOT NULL,
										 recipename			TEXT,
										 recipeIngredients	TEXT )''')
										 #TODO add more if you want


		cursor.execute('''CREATE TABLE IF NOT EXISTS
		 			  	  	savedIngredients(ingredientID			INT		PRIMARY KEY NOT NULL,
										 	 ingredient	TEXT )''')

		db.commit()
		db.close()

	def addIngredient(userID, ingredient):
		db = sqlite.connect('database.db')
		cursor = db.cursor()




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
