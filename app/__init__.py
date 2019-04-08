from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "password123"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://nathan:1234@localhost/assessment"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views