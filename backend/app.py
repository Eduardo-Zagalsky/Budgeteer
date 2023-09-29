from flask import Flask, render_template, session, redirect, flash, request
from models import db, connect_db, User, Accounts, Credit, Expenses
import jwt
from secret import SECRET_KEY, ALGORITHMS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///budgeteer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# os.environ.get(*variable name*,*hard coded name*)
app.config['SECRET_KEY'] = "secret"

connect_db(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    data = request.form[data]
    jwt.decode(data, SECRET_KEY, algorithms=[ALGORITHMS])
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
    session['user'] = user.id
    return redirect('/account-form')


@app.route('/login', methods=['POST'])
def login():
    data = request.form[data]
    jwt.decode(data, SECRET_KEY, algorithms=[ALGORITHMS])
    username = data.username
    password = data.password
    user = User.authenticate(username, password)
    if user:
        session['user'] = user.id
        return redirect('/home')


@app.route('/account-form', methods=['POST'])
def account():
    user = session['user']
    if user:
        data = request.form[data]
        jwt.decode(data, SECRET_KEY, algorithms=[ALGORITHMS])
        name = data.name
        type = data.type
        balance = data.balance
        account = Accounts(name=name, type=type,
                           balance=balance, ownerId=user)
        db.session.add(account)
        db.session.commit()
        return redirect('/credit-form')
    else:
        flash("Please sign in or make an account to add account info")
        return redirect('/home')


@app.route('/credit-form', methods=['POST'])
def credit():
    user = session['user']
    if user:
        data = request.form[data]
        jwt.decode(data, SECRET_KEY, algorithms=[ALGORITHMS])
        creditor = data.creditor
        type = data.type
        limit = data.limit
        balance = data.balance
        interest_rate = data.interest_rate
        due_date = data.due_date
        credit = Credit(creditor=creditor, type=type, limit=limit,
                        balance=balance, interest_rate=interest_rate, due_date=due_date, ownerId=user)
        db.session.add(credit)
        db.session.commit()
        return redirect('/expense-form')
    else:
        flash("Please sign in or make an account to add credit info")
        return redirect('/home')


@app.route('/expense-form', methods=['POST'])
def expense():
    user = session['user']
    if user:
        data = request.form[data]
        jwt.decode(data, SECRET_KEY, algorithms=[ALGORITHMS])
        name = data.name
        type = data.type
        amount = data.amount
        description = data.description
        date = data.date
        expense = Expenses(name=name, type=type, amount=amount,
                           description=description, date=date, ownerId=user)
        db.session.add(expense)
        db.session.commit()
        return redirect('/home')
    else:
        flash("Please sign in or make an account to add expense info")
        return redirect('/home')
