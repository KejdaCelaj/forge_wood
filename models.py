from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	productname = db.Column(db.String(100), nullable=False)
	price = db.Column(db.String(10), nullable=False)
	image = db.Column(db.String(20), nullable=False, default='default.jpg')

	def __repr__(self):
		return f"Product('{self.productname}','{self.price}','{self.image}')"
		
class EmailClub(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    street = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.firstname}', '{self.lastname}', '{self.email}', '{self.phone}', '{self.street}', '{self.city}', '{self.state}', '{self.zipcode}')"