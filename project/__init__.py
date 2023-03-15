from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate





app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://test:test@db/test'


db=SQLAlchemy(app)
migrate=Migrate(app, db)





# from project import views