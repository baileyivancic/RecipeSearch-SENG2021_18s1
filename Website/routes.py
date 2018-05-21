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

		def register_user(username, password):
			this.database.register_user(username, password)

Controller = Controller()

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/homepage")
def home():
	return render_template("homepage.html")

@app.route("/results")
def results():
	return render_template("results.html")

@app.route("/login",  methods=["GET", "POST"])
def login():
	if request.method == "POST":
		if request.form["bt"] == 'login':
			print("Login Attempt")
		if request.form["bt"] == 'register':
			return redirect(url_for("register"))
	return render_template("login.html")

@app.route("/register",  methods=["GET", "POST"])
def register():
	return render_template("register.html")

@app.route("/savedresults")
def savedresults():
	return render_template("savedresults.html")
