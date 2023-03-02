"""
This will make sure to initialize our organiser application as a package, 
allowing us to use our own imports, as well as any standard imports.
"""
import os
import re # python regular expression package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku

# ------------ Create an instance of the imported SQLAlchemy class
db = SQLAlchemy(app)


# ------------ Import file Routes will rely on the above app and db variables
from organiser import routes  # noqa
