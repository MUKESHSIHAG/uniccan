from app import app, db
from app.forms import LoginForm, RegisterForm, CreateCircleForm
from flask import render_template, redirect, url_for, flash
from app.models import User, Circle
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash(u'Invalid password provided', 'danger')
                return redirect(url_for('login'))
        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password, gender=form.gender.data, college=form.college.data, dob=form.dob.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!','success')
        return redirect(url_for('login'))
        # return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/createcircle',methods=['GET','POST'])
@login_required
def createcircle():
    form = CreateCircleForm()
    if form.validate_on_submit():
        circle = Circle(code=form.circlecode.data,title=form.title.data,description=form.description.data)
        db.session.add(circle)
        db.session.commit()
        flash('Circle created successfully!','success')
        return redirect('dashboard')
    return render_template('circle.html',form=form)
  
@app.route('/edit-profile')
def edit_profile():
    print(current_user.username, current_user.gender, current_user.dob, current_user.college)
    username = current_user.username
    gender = current_user.gender
    college = current_user.college
    dob = current_user.dob
    return render_template('profile.html',username=username,gender=gender,college=college,dob=dob)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
