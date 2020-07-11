
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


from flask_frozen import Freezer

import models
# import main
freezer = Freezer(app)


# @freezer.register_generator
# def product_details():
# for product in db.query.Product.all():
#     yield {'product_id': product.id}



if __name__ == "__main__":

    init(db)


    freezer = Freezer(app)




    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vitrine.db'
    # app.secret_key = 'super secret key'
    # app.config['SESSION_TYPE'] = 'filesystem'

    # port = int(os.environ.get('PORT', 5000))


    # app.run(host='0.0.0.0', port=port, debug=True)

    freezer.run()

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
