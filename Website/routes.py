import ast, os, time, copy
from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for, flash
from server import app
from flask_login import UserMixin
from flask_login import LoginManager,login_user, current_user, login_required, logout_user
from server import app, login_manager
from pathlib import Path
from database import Database
from datetime import datetime
import os
import sqlite3

class Controller:
		def __init__(self):
			self.database = Database()
			self.database.first_run()

		def register_user(self, username, password):
			self.database.register_user(username, password)

		def isValidUser(self, username, password):
			return self.database.isValidUser(username, password)

class User(UserMixin):
	def __init__(self, id):
		self.id = id

	def get_id(self):
		return self.id

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

@app.route("/",  methods=["GET", "POST"])
def index():
	#TODO try and put back into modal form
	return render_template("index.html")

@app.route("/login",  methods=["GET", "POST"])
def login():
	if request.method == "POST":
		if request.form["login"] == 'login':
			#TODO gonna need to user request.form.get("something", False)
			user = request.form["loginUser"]
			password = request.form["loginPass"]

			if check_password(user, password):
				print("loggedin")
				return redirect("/logged-in")
			else:
				#TODO handle not valid username and password
				pass

	return render_template("login.html")

@app.route("/register",  methods=["GET", "POST"])
def register():
	if request.method == "POST":
		if request.form["register"] == 'register':
			#TODO gonna need to user request.form.get("something", False)
			user = request.form["registerUser"]
			password = request.form["registerPass"]
			print("register Attempt: user:" + user + " pass: " + password)

			if control.register_user(user, password):
				return redirect("logged-in")
			else:
				#TODO handle not valid registration info
				return redirect(url_for("register"))
	return render_template("register.html")

@app.route("/logged-in")
@login_required
def logginIn():
	#TODO change into a proper logged in page
	return render_template("index.html")

@app.route("/homepage")
def home():
	return render_template("homepage.html")

@app.route("/results")
def results():
	return render_template("results.html")

@app.route("/savedresults")
def savedresults():
	return render_template("savedresults.html")

@app.route("/savedingredients")
def savedingredients():
	return render_template("saved-ingredients.html")

@app.route("/savedrecipes")
def savedrecipes():
	return render_template("saved-recipes.html")

@app.route("/weeklyplanner")
def weeklyplanner():
	return render_template("weekly-planner.html")
