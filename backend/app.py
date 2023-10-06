from flask import Flask, request, jsonify
from models import db, connect_db, User, Accounts, Credit, Expenses
import jwt
from secret import SECRET_KEY, ALGORITHMS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///budgeteer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
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


@app.route('/login', methods=['POST'])
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
    data = request.form[data]
    name = data.name
    type = data.type
    balance = data.balance
    user = data.user
    account = Accounts(name=name, type=type,
                       balance=balance, ownerId=user)
    db.session.add(account)
    db.session.commit()


@app.route('/credit-form', methods=['POST'])
def credit():
    data = request.form[data]
    creditor = data.creditor
    type = data.type
    limit = data.limit
    balance = data.balance
    interest_rate = data.interest_rate
    due_date = data.due_date
    user = data.user
    credit = Credit(creditor=creditor, type=type, limit=limit,
                    balance=balance, interest_rate=interest_rate, due_date=due_date, ownerId=user)
    db.session.add(credit)
    db.session.commit()


@app.route('/expense-form', methods=['POST'])
def expense():
    data = request.form[data]
    name = data.name
    type = data.type
    amount = data.amount
    description = data.description
    date = data.date
    user = data.user
    expense = Expenses(name=name, type=type, amount=amount,
                       description=description, date=date, ownerId=user)
    db.session.add(expense)
    db.session.commit()
