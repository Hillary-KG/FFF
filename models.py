
from flask_sqlalchemy import SQLAlchemy
import app

db = SQLAlchemy(app.app)

class User(db.Model):
	user_id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	email = db.Column(db.String(100),unique=True,nullable=False)
	password = db.Column(db.String(50),nullable=False)
	is_admin = db.Column(db.Integer,default=0)

	def __repr__(self):
		return [self.user_id,self.email]

class Order(db.Model):
	order_id = db.Column(db.Integer,primary_key=True)
	order_items = db.Column(db.String(500))
	total_price = db.Column(db.Float())
		

