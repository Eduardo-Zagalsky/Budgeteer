from flask import Flask, request, jsonify
from models import db, connect_db, User, Accounts, Credit, Expenses
import jwt
import os
from flask_cors import CORS
SECRET_KEY = 'hush_its_secret'  # os.getenv('SECRET_KEY')
ALGORITHMS = 'HS256'
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///budgeteer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['CORS_ORIGIN_ALLOW_ALL'] = True
app.config['SECRET_KEY'] = SECRET_KEY

connect_db(app)
with app.app_context():
    db.drop_all()
    db.create_all()


def get_user(token):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[
                          ALGORITHMS], verify=False)
        current_user = User.query.filter_by(id=data["userId"]).first()
        return current_user
    except Exception as e:
        print("Error decoding JWT", e)
        return "error"


@app.route('/signup', methods=['POST'])
def signup():
    name = request.json['formData']['name']
    email = request.json['formData']['email']
    username = request.json['formData']['username']
    password = request.json['formData']['password']
    income = request.json['formData']['income']
    credit_score = request.json['formData']['creditScore']
    user = User(full_name=name, email=email, username=username, password=User.hash(
        password), income=income, credit_score=credit_score)
    db.session.add(user)
    db.session.commit()
    auth_token = user.encode_auth_token(user.id)
    return auth_token.decode('UTF-8')


@app.route('/logon', methods=['POST'])
def login():
    username = request.json['formData']['username']
    password = request.json['formData']['password']
    user = User.authenticate(username, password)
    if user:
        auth_token = user.encode_auth_token(user.id)
        return auth_token.decode('UTF-8')
    else:
        return jsonify(403, "Sorry, you are not logged in")


@app.route('/account-form', methods=['POST'])
def account_form():
    token = request.headers.get('token')
    name = request.json['formData']['name']
    type = request.json['formData']['type']
    balance = request.json['formData']['balance']
    current_user = get_user(token)
    if current_user:
        account = Accounts(name=name, type=type,
                           balance=balance, ownerId=current_user)
        db.session.add(account)
        db.session.commit()
    else:
        return jsonify(403, "Sorry, you are not logged in")


@app.route('/credit-form', methods=['POST'])
def credit_form():
    token = request.headers.get('token')
    creditor = request.json['formData']['creditor']
    type = request.json['formData']['type']
    limit = request.json['formData']['limit']
    balance = request.json['formData']['balance']
    interest_rate = request.json['formData']['interestRate']
    due_date = request.json['formData']['dueDate']
    current_user = get_user(token)
    if current_user:
        credit = Credit(creditor=creditor, type=type, limit=limit,
                        balance=balance, interest_rate=interest_rate, due_date=due_date, ownerId=current_user.id)
        db.session.add(credit)
        db.session.commit()
    else:
        return jsonify(403, "Sorry, you are not logged in")


@app.route('/expense-form', methods=['POST'])
def expense_form():
    token = request.headers.get('token')
    name = request.json['formData']['name']
    type = request.json['formData']['type']
    amount = request.json['formData']['amount']
    description = request.json['formData']['description']
    date = request.json['formData']['date']
    current_user = get_user(token)
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
    current_user = get_user(token)
    if current_user:
        credit = Credit.query.filter_by(ownerId=current_user['userId']).all()
        return jsonify(credit)
    else:
        return jsonify(403, "Sorry, you are not logged in")


@app.route('/account', methods=['GET'])
def account():
    token = request.headers.get('token')
    current_user = get_user(token)
    if current_user:
        account = Accounts.query.filter_by(
            ownerId=current_user['userId']).all()
        return jsonify(account)
    else:
        return jsonify(403, "Sorry, you are not logged in")


@app.route('/expense', methods=['GET'])
def expense():
    token = request.headers.get('token')
    current_user = get_user(token)
    if current_user:
        expense = Expenses.query.filter_by(
            ownerId=current_user['userId']).all()
        return jsonify(expense)
    else:
        return jsonify(403, "Sorry, you are not logged in")
