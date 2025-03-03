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
# with app.app_context():
#     db.drop_all()
#     db.create_all()


def get_user(token):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[
                          ALGORITHMS], verify=False)
        resp = User.query.filter_by(id=data["userId"]).first()
        current_user = {"userId": resp.id,
                        "full_name": resp.full_name, "username": resp.username, "income": resp.income}
        return current_user
    except Exception as e:
        print("Error decoding JWT", e)
        return "error"


@app.route('/', methods=['GET'])
def page_data():
    """Home page route."""
    return jsonify(get_user(request.headers.get('token')))


@app.route('/home', methods=['GET'])
def homepage():
    """Home page route."""
    info = []
    current_user = get_user(request.headers.get('token'))
    info.append(current_user)
    if current_user:
        resp = Expenses.query.filter_by(
            ownerId=current_user['userId']).all()
        expenses = []
        for x in resp:
            item = {"name": x.name, "type": x.type, "amount": x.amount,
                    "description": x.description, "date": x.date}
            expenses.append(item)
        info.append(expenses)
        resp = Credit.query.filter_by(ownerId=current_user['userId']).all()
        credit = []
        for x in resp:
            item = {"name": current_user['full_name'], "account": x.id, "creditor": x.creditor, "type": x.type, "balance":
                    x.balance, "limit": x.limit, "interest_rate": x.interest_rate, "due_date": x.due_date}
            credit.append(item)
        info.append(credit)
        resp = Accounts.query.filter_by(ownerId=current_user['userId']).all()
        account = []
        for x in resp:
            item = {"id": x.id, "name": x.name,
                    "type": x.type, "balance": x.balance}
            account.append(item)
        info.append(account)
    return jsonify(info)


@app.route('/signup', methods=['POST'])
def signup():
    name = request.json['formData']['name']
    email = request.json['formData']['email']
    username = request.json['formData']['username']
    password = request.json['formData']['password']
    income = request.json['formData']['income']
    credit_score = request.json['formData']['creditScore']
    if User.query.filter_by(username=request.json['formData']['username']).count() > 0:
        return jsonify({"error": "Username already exists"}), 400
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
        return jsonify({"error": "Sorry, you are not logged in"}), 403


@app.route('/account-form', methods=['POST'])
def account_form():
    token = request.headers.get('token')
    name = request.json['formData']['name']
    type = request.json['formData']['type']
    balance = request.json['formData']['balance']
    current_user = get_user(token)
    print(current_user)
    if current_user:
        account = Accounts(name=name, type=type,
                           balance=balance, ownerId=current_user['userId'])
        db.session.add(account)
        db.session.commit()
        return jsonify(200, 'Account added successfully!')
    else:
        return jsonify({"error": "Sorry, you are not logged in"}), 403


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
    print(token)
    print(current_user)
    if current_user:
        credit = Credit(creditor=creditor, type=type, limit=limit,
                        balance=balance, interest_rate=interest_rate, due_date=due_date, ownerId=current_user['userId'])
        db.session.add(credit)
        db.session.commit()
        return jsonify(200, 'Credit added successfully!')
    else:
        return jsonify({"error": "Sorry, you are not logged in"}), 403


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
                           description=description, date=date, ownerId=current_user['userId'])
        db.session.add(expense)
        db.session.commit()
        return jsonify(200, 'Expense added successfully!')
    else:
        return jsonify({"error": "Sorry, you are not logged in"}), 403


@app.route('/credit', methods=['GET'])
def credit():
    token = request.headers.get('token')
    current_user = get_user(token)
    if current_user:
        resp = Credit.query.filter_by(ownerId=current_user['userId']).all()
        credit = []
        for x in resp:
            item = {"name": current_user['full_name'], "account": x.id, "creditor": x.creditor, "type": x.type, "balance":
                    x.balance, "limit": x.limit, "interest_rate": x.interest_rate, "due_date": x.due_date}
            credit.append(item)
        return jsonify(credit)
    else:
        return jsonify({"error": "Sorry, you are not logged in"}), 403


@app.route('/account', methods=['GET'])
def account():
    token = request.headers.get('token')
    current_user = get_user(token)
    if current_user:
        resp = Accounts.query.filter_by(ownerId=current_user['userId']).all()
        account = []
        for x in resp:
            item = {"id": x.id, "name": x.name,
                    "type": x.type, "balance": x.balance}
            account.append(item)
        return jsonify(account)
    else:
        return jsonify({"error": "Sorry, you are not logged in"}), 403


@app.route('/expense', methods=['GET'])
def expense():
    token = request.headers.get('token')
    current_user = get_user(token)
    info = []
    if current_user:
        info.append(current_user['income'])
        resp = Expenses.query.filter_by(
            ownerId=current_user['userId']).all()
        expenses = []
        sum = 0
        for x in resp:
            sum += x.amount
            item = {"name": x.name, "type": x.type, "amount": x.amount,
                    "description": x.description, "date": x.date}
            expenses.append(item)
        info.append(expenses)
        info.append(sum)
        return jsonify(info)
    else:
        return jsonify({"error": "Sorry, you are not logged in"}), 403
