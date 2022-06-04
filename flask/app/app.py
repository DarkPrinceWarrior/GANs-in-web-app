import models.db_setup
from flask import render_template

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from models.db_setup import db_session
from models.entities import Role

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:' \
                                        f'//postgres:{config.password}@localhost:5432/gen_Imagedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/")
def index():
    return "hello"


# @app.route("/", methods=['GET'])
# def index():
#     roles = db_session.query(Role).all()
#     return render_template('index.html', roles=roles)


if __name__ == '__main__':
    models.db_setup.init_db()
    app.run(host="0.0.0.0", debug=True)