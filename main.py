from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_mail import Mail, Message
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "library.db")
app.config['JWT_SECRET_KEY'] = "super-secret-key"
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
mail = Mail(app)


# =============================== DB Models & Schema ==========================================

class User(db.Model):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True)
    gender = Column(String)


class Book(db.Model):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    book_title = Column(String)
    author = Column(String)
    isbn = Column(String)
    publisher = Column(String)
    publication_year = Column(Integer)
    genre = Column(String)
    synopsis = Column(String)
    language = Column(String)
    page_count = Column(String)
    cover_image = Column(String)
    inventory_count = Column(Integer)
    available_count = Column(Integer)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'firstname', 'lastname', 'username', 'password', 'email', 'gender')


class BookSchema(ma.Schema):
    class Meta:
        fields = ('book_id', 'book_title', 'author', 'isbn', 'publisher', 'publication_year', 'genre', 'synopsis',
                  'language', 'page_count', 'cover_image', 'inventory_count', 'available_count')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
book_schema = BookSchema()
books_schema = BookSchema(many=True)