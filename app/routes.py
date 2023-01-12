from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from app.forms import SignUpForm, LoginForm
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
    # Create an instance of the SignUpForm class
    form = SignUpForm()
    print("FORM DATA:", form.data)
    # Check if it's a POST request AND that the data is validated
    if form.validate_on_submit():
        print("Form Submitted and Validated")
        # Get data from the form
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(email, username, password)

        check_user = User.query.filter( (User.username == username) | (User.email == email) ).all()

        if check_user:
            flash('A user with that email and/or username already exists', 'danger')
            return redirect(url_for('sign_up'))

        #TODO: Check to see if there is a User with username and/or email
        if username == 'eitanr':
            flash('That user already exists', 'danger')
            return redirect(url_for('sign_up'))
        
        new_user = User(email=email, username=username, password=password)

        #TODO: Create a new User with form data and add to the database
        #Flash a success message
        flash(f'Thank you {new_user.username} for signing up!', 'success')

        #Return to the home page after submitting and validating the user
        return redirect(url_for('index'))
        
    return render_template('sign_up.html', form = form)

@app.route('/log_in', methods=['GET','POST'])
def log_in():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(username, password)

        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            login_user(user)
            flash(f"{user.username} is now logged in!", "warning")
            return redirect(url_for('index'))
        else:
            flash("Incorrect username and/or password", "danger")
            redirect(url_for('log_in'))

    return render_template('log_in.html', form = form)

@app.route('/log_out')
def logout():
    logout_user()
    flash("You have been logged out", "warning")
    return redirect(url_for('index'))