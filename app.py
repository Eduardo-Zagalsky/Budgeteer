from flask import Flask, request, jsonify
from models import db, connect_db, User, Accounts, Credit, Expenses
import jwt
import os
from flask_cors import CORS
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHMS = 'HS256'
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///budgeteer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['CORS_ORIGIN_ALLOW_ALL'] = True
app.config['SECRET_KEY'] = SECRET_KEY

connect_db(app)


@app.route('/signup', methods=['POST'])
def signup():
    data = request.form[data]
    name = data.name
    email = data.email
    username = data.username
    password = data.password
    income = data.income
    credit_score = data.credit_score
    if income and credit_score:
        user = User(name=name, email=email, password=User.hash(
            password), income=income, credit_score=credit_score)
    elif income:
        user = User(name=name, email=email,
                    password=User.hash(password), income=income)
    elif credit_score:
        user = User(name=name, email=email, password=User.hash(
            password), credit_score=credit_score)
    else:
        user = User.register(name, email, username, password)
    db.session.add(user)
    db.session.commit()
    auth_token = user.encode_auth_token(user.id)
    return jsonify(auth_token)


@app.route('/logon', methods=['POST'])
def login():
    data = request.form[data]
    username = data.username
    password = data.password
    user = User.authenticate(username, password)
    if user:
        auth_token = user.encode_auth_token(user.id)
        return jsonify(auth_token)


@app.route('/account-form', methods=['POST'])
def account():
    token = request.headers.get('token')
    result = request.form['data']
    name = result.name
    type = result.type
    balance = result.balance
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHMS])
        current_user = User.query.first(data["userId"])
    except Exception as e:
        return e
    if current_user:
        account = Accounts(name=name, type=type,
                           balance=balance, ownerId=current_user)
        db.session.add(account)
        db.session.commit()
    else:
        return jsonify(403, "Sorry, you are not logged in")


@app.route('/credit-form', methods=['POST'])
def credit():
    token = request.headers.get('token')
    result = request.form['data']
    creditor = result.creditor
    type = result.type
    limit = result.limit
    balance = result.balance
    interest_rate = result.interest_rate
    due_date = result.due_date
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHMS])
        current_user = User.query.first(data["userId"])
    except Exception as e:
        return e
    if current_user:
        credit = Credit(creditor=creditor, type=type, limit=limit,
                        balance=balance, interest_rate=interest_rate, due_date=due_date, ownerId=current_user)
        db.session.add(credit)
        db.session.commit()
    else:
        return jsonify(403, "Sorry, you are not logged in")


@app.route('/expense-form', methods=['POST'])
def expense():
    token = request.headers.get('token')
    result = request.form['data']
    name = result.name
    type = result.type
    amount = result.amount
    description = result.description
    date = result.date
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHMS])
        current_user = User.query.first(data["userId"])
    except Exception as e:
        return e
    if current_user:
        expense = Expenses(name=name, type=type, amount=amount,
                           description=description, date=date, ownerId=current_user)
        db.session.add(expense)
        db.session.commit()
    else:
        return jsonify(403, "Sorry, you are not logged in")


@app.route('/credit', methods=['GET'])
def credit():
    token = request.headers.get('token')
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHMS])
        current_user = User.query.filter_by(data["userId"]).one()
    except Exception as e:
        return e
    if current_user:
        credit = Credit.query.filter_by(ownerId=data['userId']).all()
        return jsonify(credit)
    else:
        return jsonify(403, "Sorry, you are not logged in")
