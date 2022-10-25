**Cs50 Final Project: Curriculum Creator** 

The project is a simple curriculum generator where you enter your information and the site creates a pdf formatted with a great curriculum.

***Technologies used***

 - Flask
 - pdfkit
 - python
 - bootstrap
 - SQLAlchemy
 - Html
 - Css
 - biblioteca os 
    <hr>
    
***How the project works:***

1. You register on the site
2. Login access the curriculum creator
3. Inside the curriculum creator you have to insert all the necessary information
4. After completing the information click download
Once you click on download you will download a pdf with your resume ready

<hr>

***Routes***

The "/login" and "/register" routes do not need to be logged in, and to do this I included a helpers.py file with a decorator function called login_required and I added @login_required in all the routes where it is necessary to be logged in

To download the pdf you are directed to the route "/create_page" this route will get all the information from the curriculum creator form and will call a function called make_pdf (function included in the helpers.py file) and then you are directed to the thanks route where sera sends to download the pdf using the send_file() function

<hr>

***Database***

To make the registration system, I had to use a database "database.db" I tried for a long time to use sqlite3 but I said so I looked for something to connect flask with a database until I finally found SQLAlchemy a simple library where you can insert things into a database without using the sql language (at first I thought it was strange), but it was very difficult to figure out how to configure it because the documentation is a little confusing, but in the end everything is ok.

<hr>

***How to use***

To use the curriculum generator, you will need:

- Flask -> pip install flask
- pdfkit -> pip install pdfkit
- others

*Run*

   ```
$ export FLASK_APP=app.py
$ flask run
```

***Video URL***

<https://youtu.be/btiDorzJ45k>

