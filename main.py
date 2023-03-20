from flask import Flask,render_template
postovi = ["post1", "post2", "post3"]
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naslov = db.Column(db.String(40), unique=True)
    autor = db.Column(db.String(50))
    sadrzaj = db.Column(db.String())

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/blog")
def blog():
    return render_template("blog.html", postovi=postovi)


@app.route("/o-meni")
def o_meni():
    return render_template("index.html")
app.run(debug=True)