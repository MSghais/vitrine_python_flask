
# from mydash import app
from flask import Flask
# from flask.sql
from flask_sqlalchemy import SQLAlchemy

# from models import init_db, User, Article, Categories, Theme
# import models
# from models import *
# from main import all_views
from main import app,db

from models import User, Categories, Theme, Article
from init_db import init
import os


# from flask_frozen import Freezer

# import main

# app = Flask(__name__)

# ENV = "prod"

# if ENV == "dev":
#     app.debug = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vitrine.db'

# else:
#     app.debug = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ebbuzrqxzvdndv:1f2603a168ff4526e5b80b72905a47bc4d1a5d390e5ed3611437f88631c2c6b0@ec2-34-197-141-7.compute-1.amazonaws.com:5432/d9btjknhvpqhe9"


# init(db)

# app.run()

    


def create_app():
    ENV = "prod"

    if ENV == "dev":
        app.debug = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vitrine.db'

    else:
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ebbuzrqxzvdndv:1f2603a168ff4526e5b80b72905a47bc4d1a5d390e5ed3611437f88631c2c6b0@ec2-34-197-141-7.compute-1.amazonaws.com:5432/d9btjknhvpqhe9"


    init(db)

    app.run()

if __name__ == "__main__":

        
    ENV = "dev"

    if ENV == "dev":
        app.debug = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vitrine.db'

    else:
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ebbuzrqxzvdndv:1f2603a168ff4526e5b80b72905a47bc4d1a5d390e5ed3611437f88631c2c6b0@ec2-34-197-141-7.compute-1.amazonaws.com:5432/d9btjknhvpqhe9"


    init(db)

    app.run()


    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vitrine.db'
    # app.secret_key = 'super secret key'
    # app.config['SESSION_TYPE'] = 'filesystem'

    # port = int(os.environ.get('PORT', 5000))


    # init(db)
    # app.run(host='0.0.0.0', port=port, debug=True)

    # app.run()

# import os
# from flask_flatpages import FlatPages
# from flask_frozen import Freezer # Added
# ...
# pages = FlatPages(app)
# freezer = Freezer(app) # Added
# ...
# # Modified Main
# if __name__ == "__main__":
#     if len(sys.argv) > 1 and sys.argv[1] == "build":
#         freezer.freeze()
#     else:
#         app.run(port=8000)

#     # freez = Freezer(app)

    # freez.run()
