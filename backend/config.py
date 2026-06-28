# building the API with Flask. cors is cross-origin resource sharing, which allows the API to be accessed from different domains. os is used to access environment variables. dotenv is used to load environment variables from a .env file. logging is used to commnicate with the frontend and backend
# and will help with debugging.\

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lucysdatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)