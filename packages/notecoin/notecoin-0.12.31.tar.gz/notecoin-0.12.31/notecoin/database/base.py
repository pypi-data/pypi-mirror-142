import logging
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from notetool.secret import read_secret

app = Flask(__name__)
uri = read_secret(cate1='notecoin', cate2='app', cate3='SQLALCHEMY_DATABASE_URI')
uri = uri or f'sqlite:///{os.path.abspath(os.path.dirname(__file__))}/data/notecoin.db'

logging.info(f'uri:{uri}')

app.config['SQLALCHEMY_DATABASE_URI'] = uri
db = SQLAlchemy(app)
