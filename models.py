from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,url_for,request, g, session,logging,redirect,flash, url_for


import enum
from datetime import timedelta, datetime

from main import db
# from main_blue import db
# from init_db import init
# init(db)

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __repr__(self):
        return '<Task %r>' % self.id


class Categories(enum.Enum):

    Softs = "Softs"
    Jus = "Jus"
    Café = "Café"
    Thé = "Thé"

    Vins = "Vins"
    Bières = "Bières"
    Spiritueux = "Spiritueux"

    Chips="Chips"
    Fromages="Fromages"
    Charcuterie="Charcuterie"

    Freez="Freez & Glaces"

    Surgelés = "Surgelés"


    Fruit="Fruit"
    Légumes="Légumes"

    Confisseries = "Confisseries"
    Epicerie="Epicerie"
    Gateaux="Gateaux"
    Sucreries="Sucreries"

    Champoing = "Champoing"
    Gel = "Gel"
    Deodorant = "Déodorant"

    Chichas = "Chichas"
    Charbon = "Charbon"
    Briquets = "Briquets"

    Vitrine = "Lave vitrine"
    Sol = "Sol"
    Meuble= "Meubles"
    Savons = "Savons"

# class Theme(db.Model):
#     # id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), primary_key=True)
#     categories = db.Column(db.Enum(Categories))

#     def __repr__(self):
#         return '<Task %r>' % self.id

class Theme(enum.Enum):

    Alimentaire = "Alimentaire"
    Boissons = "Boissons"

    US = "US Products"
    Menagers = "Produits Ménagers"
    Hygyene = "Hygiène"
    Divers = "Produits Divers"
    Accessoires = "Accessoires"



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    login = db.Column(db.String(200), nullable=False)
    password= db.Column(db.String(200), nullable=False)
    # todos = db.relationship('Todo', backref='owner')
    # posts = db.relationship('Blogpost', backref='owner')
    # subscriptions = db.relationship('channel', secondary=subscribers, backref=db.backref('subscribers') , lazy= 'dynamic'  ) 
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    # owner_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    # channel_id = db.Column(db.Integer, db.ForeignKey('Channel.id'))
    def __repr__(self):
        return '<Task %r>' % self.id

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prix = db.Column(db.Float(100), nullable=False)
    promotions = db.Column(db.Float(100), nullable=True)

    quantites = db.Column(db.Integer, nullable=True)


    content = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(100), nullable=True)
    
    theme = db.Column(db.Enum(Theme))

    # theme = db.Column(db.Integer, db.ForeignKey('theme.name'))
    # theme_back = db.relationship('Theme',
    #     backref=db.backref('article_theme', lazy=True))

    categories = db.Column(db.Enum(Categories))


    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
         return '<Task %r>' % self.id
         
# class MyTable(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     fruit_type = db.Column(db.Enum(FruitType))
    

# subscribers = db.Table('subscribers',
# db.Column('user_id', db.Integer, db.ForeignKey('user.id') ),
# db.Column('channel_id', db.Integer, db.ForeignKey('channel.id') )


#    )



# class Channel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30))

#     def __repr__(self):
#         return '<Task %r>' % self.id


# class Categories(enum.Enum):

#     Softs = "Softs"
#     Jus = "Jus"
#     Café = "Café"
#     Thé = "Thé"

#     Vins = "Vins"
#     Bières = "Bières"
#     Spiritueux = "Spiritueux"

#     Chips="Chips"
#     Fromages="Fromages"
#     Charcuterie="Charcuterie"

#     Fruit="Fruit"
#     Légumes="Légumes"

#     Confisseries = "Confisseries"
#     Epicerie="Epicerie"
#     Gateaux="Gateaux"
#     Sucreries="Sucreries"

#     Champoing = "Champoing"
#     Gel = "Gel"
#     Deodorant = "Déodorant"

#     Chichas = "Chichas"
#     Charbon = "Charbon"
#     Briquets = "Briquets"

#     Vitrine = "Lave vitrine"
#     Sol = "Sol"
#     Meuble= "Meubles"
#     Savons = "Savons"

# # class Theme(db.Model):
# #     # id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String(30), primary_key=True)
# #     categories = db.Column(db.Enum(Categories))

# #     def __repr__(self):
# #         return '<Task %r>' % self.id

# class Theme(enum.Enum):

#     Alimentaire = "Alimentaire"
#     Boissons = "Boissons"

#     US = "US Products"
#     Menagers = "Produits Ménagers"
#     Hygyene = "Hygiène"
#     Divers = "Produits Divers"
#     Accessoires = "Accessoires"



# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(200), nullable=False)
#     login = db.Column(db.String(200), nullable=False)
#     password= db.Column(db.String(200), nullable=False)
#     # todos = db.relationship('Todo', backref='owner')
#     # posts = db.relationship('Blogpost', backref='owner')
#     # subscriptions = db.relationship('channel', secondary=subscribers, backref=db.backref('subscribers') , lazy= 'dynamic'  ) 
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Task %r>' % self.id


# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#     # owner_id = db.Column(db.Integer, db.ForeignKey('User.id'))
#     # channel_id = db.Column(db.Integer, db.ForeignKey('Channel.id'))
#     def __repr__(self):
#         return '<Task %r>' % self.id

# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nom = db.Column(db.String(100), nullable=False)
#     prix = db.Column(db.Float(100), nullable=False)
#     promotions = db.Column(db.Float(100), nullable=True)

#     quantites = db.Column(db.Integer, nullable=True)


#     content = db.Column(db.Text, nullable=True)
#     image = db.Column(db.String(100), nullable=True)
    
#     theme = db.Column(db.Enum(Theme))

#     # theme = db.Column(db.Integer, db.ForeignKey('theme.name'))
#     # theme_back = db.relationship('Theme',
#     #     backref=db.backref('article_theme', lazy=True))

#     categories = db.Column(db.Enum(Categories))


#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     def __repr__(self):
#          return '<Task %r>' % self.id
         
# class MyTable(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     fruit_type = db.Column(db.Enum(FruitType))
    

# subscribers = db.Table('subscribers',
# db.Column('user_id', db.Integer, db.ForeignKey('user.id') ),
# db.Column('channel_id', db.Integer, db.ForeignKey('channel.id') )


#    )














    # db = SQLAlchemy(app)

