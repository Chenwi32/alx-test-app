from pickle import FALSE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 