from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, FloatField, IntegerField, DateField, SelectField
from wtforms.validators import InputRequired, Length


class AddUserForm(FlaskForm):
    name = StringField("Full Name", validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired()])
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired(), Length(
        min=8, max=20, message="password is either too short or too long")])
    income = FloatField('Income', validators=[InputRequired()])
    credit_score = IntegerField('Credit Score', validators=[InputRequired()])


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class CreditForm(FlaskForm):
    creditor = StringField("Creditor", validators=[InputRequired()])
    type = StringField("Type of Credit", validators=[InputRequired()])
    limit = IntegerField("Credit Limit")
    balance = FloatField("Balance", validators=[InputRequired()])
    interest_rate = FloatField("Interest Rate", validators=[InputRequired()])
    due_date = DateField("Due Date", validators=[InputRequired()])


class ExpenseForm(FlaskForm):
    name = StringField('Expense', validators=[InputRequired()])
    type = StringField('Type')
    amount = FloatField('Amount', validators=[InputRequired()])
    description = StringField('Description', validators=[InputRequired()])
    date = DateField('Date', validators=[InputRequired()])


class AccountForm(FlaskForm):
    name = StringField("Bank Name", validators=[InputRequired()])
    type = StringField("Account Type", validators=[InputRequired()])
    balance = FloatField("Balance", validators=[InputRequired()])
