from flask import Flask
from models import db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///*database*'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"

connect_db(app)


@app.route('/flask', methods=['GET'])
def index():
    return "Flask server"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
