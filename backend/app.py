from flask import Flask, render_template, session, redirect, flash
from models import db, connect_db, User, Accounts, Credit, Expenses

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///*database*'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"

connect_db(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = AddUserForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        income = form.income.data
        credit_score = form.credit_score.data
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
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.authenticate(username, password)
        if user:
            session['user'] = user.id
            return redirect('/home')
        else:
            form.username.errors = ["Incorrect Username/Password"]
    return render_template("login.html", form=form)


@app.route('/account-form', methods=['GET', 'POST'])
def account():
    user = session['user']
    if user:
        form = AccountForm()
        if form.validate_on_submit():
            name = form.name.data
            type = form.type.data
            balance = form.balance.data
            account = Accounts(name=name, type=type,
                               balance=balance, ownerId=user)
            db.session.add(account)
            db.session.commit()
            return redirect('/credit-form')
        return render_template('accounts.html', form=form)
    else:
        flash("Please sign in or make an account to add account info")
        return redirect('/home')


@app.route('/credit-form', methods=['GET', 'POST'])
def credit():
    user = session['user']
    if user:
        form = CreditForm()
        if form.validate_on_submit():
            creditor = form.creditor.data
            type = form.type.data
            limit = form.limit.data
            balance = form.balance.data
            interest_rate = form.interest_rate.data
            due_date = form.due_date.data
            credit = Credit(creditor=creditor, type=type, limit=limit,
                            balance=balance, interest_rate=interest_rate, due_date=due_date, ownerId=user)
            db.session.add(credit)
            db.session.commit()
            return redirect('/expense-form')
        return render_template('credit.html', form=form)
    else:
        flash("Please sign in or make an account to add credit info")
        return redirect('/home')


@app.route('/expense-form', methods=['GET', 'POST'])
def expense():
    user = session['user']
    if user:
        form = ExpenseForm()
        if form.validate_on_submit():
            name = form.name.data
            type = form.type.data
            amount = form.amount.data
            description = form.description.data
            date = form.date.data
            expense = Expenses(name=name, type=type, amount=amount,
                               description=description, date=date, ownerId=user)
            db.session.add(expense)
            db.session.commit()
            return redirect('/home')
        return render_template('expenses.html', form=form)
    else:
        flash("Please sign in or make an account to add expense info")
        return redirect('/home')
