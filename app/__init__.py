from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

import yaml

with open('config.yaml', "r") as f:
    config = yaml.load(f)


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = config['database']
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

from app import apis, models
