from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
import sqlite3
from selenium.webdriver.common.keys import Keys
import os.path

engine = create_engine('sqlite://',
                       connect_args={'check_same_thread': False},
                       poolclass=StaticPool)

db = SQLAlchemy()
app = Flask(__name__)
db_name = 'company-contacts.db'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
db_path = os.path.join(BASE_DIR, db_name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)


class Companies(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(250), nullable=False, unique=True)
    award = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250))
    phone_number = db.Column(db.String(250))
    address = db.Column(db.String(250))


class Sample(db.Model):
    __tablename__ = 'sample'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(250), nullable=False, unique=True)
    award = db.Column(db.String(250), nullable=False)
    link = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250))
    phone_number = db.Column(db.String(250))
    address = db.Column(db.String(250))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/company_contacts')
def company_contacts():
    try:
        contact_info = db.session.execute(db.select(Sample))
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
    return render_template('company_contacts.html', contacts=contact_info)

if __name__ == '__main__':
    app.run(debug=True)
