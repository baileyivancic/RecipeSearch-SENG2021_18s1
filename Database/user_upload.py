# only to be used once, since after the initial execution everything is in the database

from user import *
from server import *
from werkzeug.security import generate_password_hash, check_password_hash 
import csv

with open("csv_files/passwords.csv", "r") as csv_in:
	reader = csv.reader(csv_in)
	for row in reader:
		uid = row[0]
		password = row[1]
		user_type = row[2]
		hashed_password = generate_password_hash(password)
		if not user_exists(uid, hashed_password, user_type):
			u = new_user(uid, hashed_password, user_type)
			add_to_db(u)
	# create admin user
	hashed_admin_pass = generate_password_hash("admin_password")
	admin = new_user(0, hashed_admin_pass, "admin")
	add_to_db(admin)


commit_db()



