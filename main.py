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
# app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
# app.config['MAIL_PORT'] = 2525
# app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
# app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False

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


# =============================== CLI Commands ==========================================

@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database created with success")


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print("Database dropped with success")


@app.cli.command('db_seed')
def db_seed():
    test_user = User(
        firstname="John",
        lastname="Smith",
        username="jsapi",
        password="qwerty",
        email="js@test.tst",
        gender="M"
    )

    test_book = Book(
        book_title="Learning Python, 5th Edition",
        author="Mark Lutz",
        isbn="1449355730",
        publisher="O'Reilly Media",
        publication_year=2013,
        genre="Programming",
        synopsis="Get a comprehensive, in-depth introduction to the core Python language with this hands-on book. "
                 "Based on author Mark Lutz’s popular training course, this updated fifth edition will help you "
                 "quickly write efficient, high-quality code with Python. It’s an ideal way to begin, whether "
                 "you’re new to programming or a professional developer versed in other languages.",
        language="English",
        page_count=1643,
        cover_image="https://m.media-amazon.com/images/I/91RcdlPx1CL._SY466_.jpg",
        inventory_count=5,
        available_count=5
    )

    db.session.add(test_user)
    db.session.add(test_book)
    db.session.commit()


# =============================== API Routes ==========================================

@app.route('/')
def index():
    return jsonify(message="Library API created using Python and Flask Web Framework")


@app.route('/book_list', methods=['GET'])
def book_list():
    all_books = Book.query.all()
    result = books_schema.dump(all_books)
    return jsonify(result)


@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    username = request.form['username']
    email_in = User.query.filter_by(email=email).first()
    username_in = User.query.filter_by(username=username).first()
    if email_in or username_in:
        return jsonify("Username and/or email are already in our system")
    else:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        password = request.form['password']
        gender = request.form['gender']
        user = User(firstname=firstname, lastname=lastname, username=username, password=password, email=email,
                    gender=gender)
        db.session.add(user)
        db.session.commit()
        return jsonify(message="New user registered with success")


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try_login = User.query.filter_by(username=username, password=password).first()

    if try_login:
        access_token = create_access_token(identity=username)
        return jsonify(message="You are logged in successfully", access_token=access_token)
    else:
        return jsonify(message="Your username and/or password are wrong")


@app.route('/add_book', methods=['POST'])
def add_book():
    pass


@app.route('/edit_book/<int:book_id>')
def edit_book(book_id):
    pass


@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    pass


@app.route('/book_details/<int:book_id>')
def book_details(book_id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
