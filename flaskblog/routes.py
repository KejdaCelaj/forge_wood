from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, JoinEmail, ProductForm
from flaskblog.models import User, Product, EmailClub
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def home():
    
    return render_template("home.html")

@app.route('/join_email/', methods=['GET', 'POST'])
def join_email():
    form = JoinEmail()
    if form.validate_on_submit():
        subscriber = EmailClub(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data,
            phone=form.phone.data, street=form.street.data, city=form.city.data, state=form.state.data, zipcode=form.zipcode.data)
        db.session.add(subscriber)
        db.session.commit()
        flash('Your have been succcessfully entered to our email list!', 'success')
        return redirect(url_for('home'))
    return render_template("join_email.html",title="JoinEmail", form=form)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form=ProductForm()
    if form.validate_on_submit():
        product = Product(productname=form.productname.data, price=form.price.data, image=form.image.data)
        db.session.add(product)
        db.session.commit()
        flash('Your have succcessfully entered a new product','success')
        return redirect(url_for('home'))
    return render_template("add_product.html",title="AddProduct",form=form)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/accents')
def accents():
    return render_template("accents.html")

@app.route('/ho1')
def ho1():
    return render_template("ho1.html")

@app.route('/bedroom')
def bedroom():
    return render_template("bedroom.html")

@app.route('/dining_room')
def dining_room():
    return render_template("dining_room.html")

@app.route('/entertainment')
def entertainment():
    return render_template("entertainment.html")

@app.route('/home_office')
def home_office():
    return render_template("home_office.html")

@app.route('/living_room')
def living_room():
    return render_template("living_room.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

    
if __name__ == "__main__":
    app.run(debug=True)