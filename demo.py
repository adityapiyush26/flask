from flask import Flask, render_template, url_for, flash, redirect,request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/recruitment")
def recruitment():
    return render_template('recruitment.html')

@app.route("/society")
def society():
    return render_template('society.html')

@app.route("/invitation")
def invitation():
    return render_template('invitation.html')

@app.route("/events")
def events():
    return render_template('events.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/insti_culture")
def insti_culture():
    return render_template('insti_culture.html')

@app.route("/posts")
def posts():
    return render_template('posts.html')

@app.route("/calender")
def calender():
    return render_template('calender.html')


@app.route("/register")
def register():
	if(request.method=='POST'):

	        username = request.form.get('username')
	        email = request.form.get('email')
	        imgfile = request.form.get('image_file')
	        cov_imgfile = request.form.get('image_file')
	        password = request.form.get('password')
	        post = request.form.get('posts')
	        entry = Contacts(username=username, email = email, image_file = imgfile, password = password )
	        db.session.add(entry)
	        db.session.commit()
    	return render_template('register.html')

@app.route("/login")
def login():
    return render_template('login.html')


app.run(debug=True)