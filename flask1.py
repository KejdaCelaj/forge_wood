from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '39e2300e7fdcc296ad38ccb591f49829'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contact_us/')
def contact_us():
    return render_template("contact_us.html")

@app.route('/join_email/')
def join_email():
    return render_template("join_email.html")

@app.route('/room_planner/')
def room_planner():
    return render_template("room_planner.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)