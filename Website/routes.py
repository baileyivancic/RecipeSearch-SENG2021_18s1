import ast, os, time, copy
from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for, flash
from server import app


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/homepage")
def home():
	return render_template("homepage.html")

@app.route("/results")
def results():
	return render_template("results.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/register")
def register():
	return render_template("register.html")

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
