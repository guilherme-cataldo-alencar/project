from flask import redirect, render_template, request, session
from fpdf import FPDF
from functools import wraps
import pdfkit


#TODO
def make_pdf(output, name, email,phone_number, district, street, city, birthday, objective, scholarity, level, state):
    html_response = """ 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <center>
            <h1>"""+name.title()+"""</h1>
            <br>
        </center>

        <div>
            <h2>Personal Information</h2>
            <p>District: """+district+"""
            <p>City: """+city+""" """+state.upper()+"""</p>
            <p>Street: """+street+"""</p>
            <p>Email: """+email+"""</p>
            <p>Phone Number: """+phone_number+"""+</p>
            <p>Birthday: """+birthday+"""</p>
        </div>

        <hr>

        <div>
            <h2>Objective</h2>
            <p>"""+objective+"""</p>
        </div>

        <div>
            <h2>Scholarity</h2>
            <p>"""+scholarity+"""</p>
            <p>"""+level+"""</p>
        </div>
    </body>
    </html>
    """
    pdfkit.from_string(html_response, output)


#DONE
def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
