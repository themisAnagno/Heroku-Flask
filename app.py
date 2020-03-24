import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db
from resources.user import UserRegister
from resources.item import Item, ItemList
from security import authentication, identity

app = Flask(__name__)
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
try:
    app.secret_key = os.environ["SECRET"]
except KeyError:
    app.secret_key = "secret"
jwt = JWT(app, authentication, identity)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/")
def home():
    return "Hello, world"


if __name__ == "__main__":
    db.init_app(app)
    app.run(host="0.0.0.0", port=8013, debug=True)
