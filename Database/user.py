from server import db, recipe_user_table, user_ingredient_table
from flask_login import UserMixin

class User(db.Model, UserMixin):

	__tablename__ = "user"
	user_id = db.Column(db.Integer, primary_key=True)
	password = db.Column(db.String(50), nullable=False)
	user_type = db.Column(db.String(20), nullable=False)
	recipes = db.relationship("Recipes", secondary=recipe_user_table,
		lazy="subquery", backref=db.backref("user", lazy=True))
	ingredients = db.relationship("Ingredients", secondary=user_ingredient_table,
		lazy=True, backref=db.backref("users", lazy=True))
