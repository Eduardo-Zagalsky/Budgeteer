from unittest import TestCase
from app import app
from models import db, User, Accounts, Credit, Expenses
import jwt
SECRET_KEY = 'hush_its_secret'
ALGORITHMS = 'HS256'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_budgeteer'
app.config['SQLALCHEMY_ECHO'] = False
app.config['Testing'] = True

db.drop_all()
db.create_all()


class FormTest(TestCase):
    def setUp(self):
        db.session.query(User).delete()
        self.testuser = User.register(
            name="Test", email="test@test.com", username="testuser", pwd="testuser")
        db.session.add(self.testuser)
        db.session.commit()
        self.token = self.testuser.encode_auth_token(
            self.testuser.id).decode('UTF-8')

    def test_user(self):
        user = User(full_name="John Smith", email="johnsmith@email.com",
                    username="JohnDoe", password="password")
        db.session.add(user)
        db.session.commit()
        users = User.query.filter_by(full_name="John Smith").first()
        self.assertEqual(users.full_name, "John Smith")

    def test_signup(self):
        with app.test_client() as client:
            # testing adding a new user
            json = {"formData": {"name": "Jane Doe", "email": "janedoe@email.com",
                                 "username": "JaneDoe", "password": "password", "income": "50000", "creditScore": "700"}}
            resp = client.post("/signup", json=json,
                               headers={"Content-Type": "application/json"})
            # test signup for new user
            user = User.query.filter_by(email="janedoe@email.com").first()
            self.assertEqual(user.full_name, "Jane Doe")

    def test_login(self):
        with app.test_client() as client:
            # add an existing user to database before login tests can be performed
            resp = client.post(
                "/login", json={"username": "testuser", "password": "testuser"})
            print(resp.get_data(as_text=True))
            # test login for existing user
            user = User.query.filter_by(username="testuser").first()
            self.assertEqual(user.full_name, "Test")

    def test_fail_signup(self):
        with app.test_client() as client:
            # testing adding an existing user
            resp = client.post("/signup", data={"full_name": "Jane Doe", "email": "janedoe@email.com",
                                                "username": "JaneDoe", "password": "password"})
            self.assertEqual(resp.status_code, 400)

    def test_account(self):
        with app.test_client() as client:
            # add account info
            json = {"formData": {"name": "Test Bank",
                                 "type": "checking", "balance": "2000"}}
            resp = client.post(
                "/account-form", json=json, headers={"token": self.token, "Content-Type": "application/json"})
            # get the first checking account
            account = Accounts.query.filter_by(type="checking").first()
            # test
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(account.name, "Test Bank")

    def test_credit(self):
        with app.test_client() as client:
            # add credit info
            json = {"formData": {"creditor": "Test Bank", "type": "credit card",
                                 "limit": "2000", "balance": "1000", "interestRate": "20", "dueDate": "01/01/2025"}}
            resp = client.post("/credit-form", json=json,
                               headers={"token": self.token, "Content-Type": "application/json"})
            # get the first credit card
            credit = Credit.query.filter_by(type="credit card").first()
            # test
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(credit.limit, 2000)
            self.assertEqual(credit.balance, 1000)

    def test_expense(self):
        with app.test_client() as client:
            # add expense info
            json = {"formData": {"name": "Test Properties", "type": "rent",
                                 "amount": "1000", "description": "rent payment", "date": "01/01/2025"}}
            resp = client.post(
                "/expense-form", json=json, headers={"token": self.token, "Content-Type": "application/json"})
            # get the first expense
            expense = Expenses.query.filter_by(type="rent").first()
            # test
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(expense.name, "Test Properties")
            self.assertEqual(expense.amount, 1000)
