from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

""" This initializes our flask app """
app = Flask(__name__)

""" This config is to get rid of some extra warnings coming from sqlalchemy """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

""" This will links our app to a database """
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sbgqoigdmefzjv:ac2ad6e6450609e5694af3d94aa974477f9170ffce34e4e0ad4d073ed5ce8706@ec2-52-86-115-245.compute-1.amazonaws.com:5432/deb2b2ueb3stq2'

""" This will instantiate the dabase module and  will link our flask app to sqlAlchemy """
db = SQLAlchemy(app)


""" This will allow us to be able to use the flask migrate comands to generate, upgrade, downgrade """
migrate = Migrate(app, db)

""" This will use sqlalchemy under the hood to map from classes to tables""" 
class Todo (db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id}, name: {self.description} '


""" class FoundIds(db.Model):
    __tablename__ = 'ids'
    id = db.Column(db.Integer, primary_key=True)
    contact = db.Column(db.String(), nullable=False)
    location = db.Column(db.String()) """

""" This will then create all the tables we are manipulating above if they don't exist yet, if they already do exist, then it will simply not do anything 
db.create_all()"""

""" We can still send data to the database without directly writing code in this file using the python3 terminal with this commands

    >> import flask_psql_app
    >> from flask_psql_app import db, Person
    >> person = Person(name='Ernest')
    >> db.session.add(person)
    >> db.session.commit()

 """

@app.route('/')

def index():
    
    todos = Todo.query.filter(Todo.description == 'Finsh lesson today').first() 
     
    return 'Hello ' + todos.description





