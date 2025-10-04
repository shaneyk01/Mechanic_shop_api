from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase




app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
ma = Marshmallow()
