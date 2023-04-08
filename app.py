from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config.update(SQLALCHEMY_ECHO=True)

db = SQLAlchemy(app)
# db.init_app(app)

# with app.app_context():
#     db.create_all()

from routes import *

if __name__ == '__main__':
    app.run(debug=True, port=5002)
# db.create_all()