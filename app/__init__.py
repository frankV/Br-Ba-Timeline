import os, sys
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

app = Flask(__name__, static_url_path='')
db = SQLAlchemy(app)

# from app.models import episode
from app.routes import controllers
from app.routes import episodes