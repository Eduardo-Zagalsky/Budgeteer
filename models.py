from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import jwt
import os
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHMS = 'HS256'

db = SQLAlchemy()
bcrypt = Bcrypt()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    income = db.Column(db.Float)
    credit_score = db.Column(db.Integer)
    credit = db.relationship('Credit')
    account = db.relationship('Accounts')
    expense = db.relationship('Expenses')

    @classmethod
    def hash(cls, pwd):
        return bcrypt.generate_password_hash(pwd).decode("utf-8")

    @classmethod
    def register(cls, name, email, username, pwd):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(pwd)

        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed_utf8, name=name, email=email)

    @classmethod
    def authenticate(cls, username, pwd):
        """
        Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False

    def encode_auth_token(self, user_id):
        try:
            u = User.query.filter_by(id=user_id).first()
            payload = {'userId': u.id, 'name': u.name, 'username': u.username}
            return jwt.encode(payload, SECRET_KEY, algorithm=[ALGORITHMS])
        except Exception as e:
            return e


class Accounts(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'))


class Credit(db.Model):
    __tablename__ = 'credit'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creditor = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    limit = db.Column(db.Float)
    interest_rate = db.Column(db.Float, nullable=False)
    due_date = db.Column(db.Integer, nullable=False)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'))


class Expenses(db.Model):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    expenseType = db.Column(db.Text)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'))
