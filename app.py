"""
    FAZER SISTEMA DE ADICIONAR CURSOS (ULTIMA PARTE)
"""

import os
from flask import Flask, send_file, request, render_template, redirect, url_for, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from helpers import make_pdf, login_required
from sqlalchemy.sql import func
import pdfkit

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


# DONE
@app.route("/", methods=["GET", "POST"])
@login_required
def index():
   	return render_template("index.html", name="")


# DONE
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        user = Users(firstname=name,
            email=email,
            password=password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")


# DONE
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        email = request.form.get("email")
        password = request.form.get("password")

        rows = Users.query.filter_by(email=email).all()

        if len(rows) == 1:
            if rows[0].password == password:
                session["user_id"] = rows[0].id
                return redirect("/")
    else:
        return render_template("login.html")


# DONE
@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    session["user_id"] = None
    return redirect("/login")

@app.route("/thanks")
@login_required
def thanks():
    path = "output.pdf"
    return send_file(path, as_attachment=True)

@app.route("/create_page",methods=["GET","POST"])
def create_page():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")

        birthday = request.form.get("birthday")
        country = request.form.get("country")
        state = request.form.get("state")
        city = request.form.get("city")
        disctrict = request.form.get("disctrict")
        street = request.form.get("street")

        objective = request.form.get("objective")

        scholarity = request.form.get("scholarity")
        level = request.form.get("level")

        local = request.form.get("local")
        course = request.form.get("course")
        workload = request.form.get("workload")


        make_pdf("output.pdf", name, email,  phone, disctrict, street, city, birthday, objective, scholarity, level,state)

    return redirect("/thanks")



