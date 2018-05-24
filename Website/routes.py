import ast, os, time, copy
from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for, flash, request, Response
from server import app
from flask_login import UserMixin
from flask_login import LoginManager,login_user, current_user, login_required, logout_user
import json
from server import app, login_manager
from pathlib import Path
from database import Database
from datetime import datetime
import os
import sqlite3
import sys
import random
import json
from pprint import pprint


class Controller:
		def __init__(self):
			self.database = Database()
			self.database.first_run()

		def register_user(self, username, password):
			return self.database.register_user(username, password)

		def isValidUser(self, username, password):
			return self.database.isValidUser(username, password)
		def getSavedIng(self,userID):
			return self.database.getSavedIng(userID)

		def addIng(self,ing,userID):
			return self.database.addIng(ing,userID)

		def delIng(self,ing,userID):
			return self.database.delIng(ing,userID)


class User(UserMixin):
	def __init__(self, id):
		self.id = id

	def get_id(self):
		return self.id

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

control = Controller()

def check_password(user_id, password):
	if control.isValidUser(user_id, password):
		user = User(user_id)
		login_user(user)
		return True
	return False

def get_user(user_id):

	return User(user_id)

@login_manager.user_loader
def load_user(user_id):
	# get user information from db
	user = get_user(user_id)
	return user

login_manager.login_view = "login"
login_manager.login_message = "Welcome"

@app.route("/",  methods=["GET", "POST"])
def index():
	return render_template("index.html", loggedin = 0)

@app.route("/logout",  methods=["GET", "POST"])
@login_required
def logout():
	logout_user()
	return render_template("index.html", loggedin = 0)


@app.route("/login",  methods=["GET", "POST"])
def login():
	if request.method == "POST":
		if request.form["login"] == 'login':
			user = request.form["loginUser"].strip()
			password = request.form["loginPass"].strip()

			if check_password(user, password):
				login_user(User(user), remember= False)
				return redirect("/logged-in")
			else:
				return render_template("login.html", response=0)


	return render_template("login.html", response= 1)

@app.route("/register",  methods=["GET", "POST"])
def register():
	if request.method == "POST":
		if request.form["register"] == 'register':
			user = request.form["registerUser"].strip()
			password = request.form["registerPass"].strip()
			print("register Attempt: user:" + user + " pass: " + password)
			valid = control.register_user(user, password)
			if valid == 1:
				login_user(User(user), remember= False)
				return redirect("/logged-in")
			else:
				return render_template("register.html", response=0)

	return render_template("register.html", response=1)

@app.route("/logged-in")
@login_required
def logginInIndex():
	return render_template("index.html", loggedin = 1)

#TODO find out how many other pages need to be managed
@app.route("/homepage")
def home():
	return render_template("homepage.html")

@app.route("/results")
def results():
	return render_template("results.html", loggedin=0)

@app.route("/results-logged", methods=["GET"])
@login_required
def resultsLogged():
	return render_template("results.html", loggedin=1)

@app.route("/reciever", methods=["POST"])
def getdata():
	print("Printing:")
	data = request.form.get('recobj')
	print(data)
	
	#print("data: ", data)
	# pprint(request.get_data())
	# j = json.loads(request.get_data())
	# pprint(j)
	print("1")
	#print(request.data)
	result = ''
	# for item in data:
	# 	# loop over every row
	# 	result += str(item['make']) + '\n'
	# 	print(result)

	return Response(result, mimetype='application/json')

@app.route("/savedresults")
@login_required
def savedresults():
	return render_template("savedresults.html")


@app.route("/delIng/<data>", methods=['GET'])
def removeDBIngredient(data):
	control.delIng(data,current_user.get_id())
	return (''),204

@app.route("/addIng/<data>",methods=['GET'])
def addDBIngredient(data):
	control.addIng(data,current_user.get_id())
	return (''),204

@app.route("/savedingredients")
@login_required
def savedingredients():
	ings = control.getSavedIng(current_user.get_id())
	return render_template("saved-ingredients.html",ingredients = ings)

@app.route("/savedrecipes")
@login_required
def savedrecipes():
	return render_template("saved-recipes.html")

@app.route("/weeklyplanner")
@login_required
def weeklyplanner():
	return render_template("weekly-planner.html")
