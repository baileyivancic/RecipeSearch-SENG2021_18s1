from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# table is for the relationship between saved recipes and user
recipe_user_table = db.Table("recipe_user_table",
	db.Column("user_id", db.Integer, db.ForeignKey("user.user_id"), primary_key=True), #Recipe id stuff, does edamam take care of this?
	db.Column("recipe_id", db.Integer, db.ForeignKey("recipe.course_id"), primary_key=True)
)

# table is for the relationship between user and ingredients
user_ingredient_table = db.Table("user_ingredient_table", 
	db.Column("user_id", db.Integer, db.ForeignKey("user.user_id"), primary_key=True),
	db.Column("ingredient", db.String[20], primary_key=True) 
)

def add_to_db(item):
	db.session.add(item)

def commit_db():
	db.session.commit()

def remove_from_db(item):
	db.session.delete(item) 