from unittest import TestCase
from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_budgeteer'
app.config['SQLALCHEMY_ECHO'] = False
app.config['Testing'] = True

db.drop_all()
db.create_all()


class FormTest(TestCase):
    def setUp(self):
        db.session.query(User).delete()
        self.testuser = User.register(
            full_name="Test", email="test@test.com", username="testuser", password="testuser")
        db.session.add(self.testuser)
        db.session.commit()

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
            resp = client.post("/signup", data={"full_name": "Jane Doe", "email": "janedoe@email.com",
                                                "username": "JaneDoe", "password": "password"})
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
            print(user)
            self.assertEqual(user.full_name, "Test")
