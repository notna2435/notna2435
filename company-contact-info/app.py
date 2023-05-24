from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
import sqlite3
from selenium.webdriver.common.keys import Keys
import os.path
import random
import string
import time

engine = create_engine('sqlite://',
                       connect_args={'check_same_thread': False},
                       poolclass=StaticPool)
app = Flask(__name__)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)
# db_name = 'company-contacts.db'
# db_path = os.path.join(BASE_DIR, db_name)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///company-contacts.db'
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'company-contacts.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'sample_python'
db = SQLAlchemy(app)


class Companies(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(250), nullable=False, unique=True)
    award = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250))
    phone_number = db.Column(db.String(250))
    address = db.Column(db.String(250))


class Sample(db.Model):
    # __tablename__ = 'sample'
    id = db.Column(db.Integer, primary_key=True, unique=False)
    company_name = db.Column(db.String(250), nullable=False, unique=False)
    award = db.Column(db.String(250), nullable=False, unique=False)
    link = db.Column(db.String(250), nullable=False, unique=False)
    email = db.Column(db.String(250), unique=False)
    phone_number = db.Column(db.String(250), unique=False)
    address = db.Column(db.String(250), unique=False)

def get_random_string(length): 
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

# with app.app_context():
#     db.create_all()
#     new_item = Sample(company_name=get_random_string(2), award=get_random_string(4), link=get_random_string(5),
#                               email=get_random_string(6), phone_number=get_random_string(5), address=get_random_string(6))
#     db.session.add(new_item)
#     db.session.commit()
time.sleep(2)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/company_contacts')
def company_contacts():
    # db.session.execute(db.select(User).order_by(User.username)).scalars()
    try:
        contact_info = Sample.query.all()
        # contact_info =  db.session.execute(db.select(Sample)).scalars()
        print('ffsdfs', contact_info)
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
    return render_template('company_contacts.html', contacts=contact_info)

if __name__ == '__main__':
    # db.init_app(app)
    app.run(debug=True)
