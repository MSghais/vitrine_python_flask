from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,url_for,request, g, session,logging,redirect,flash, url_for


import enum
from datetime import timedelta, datetime

# models = Blueprint("models", __name__)
# from main_blue import db

# from main import db

# from main_blue import db



from models import Article, Categories, Theme



import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# def init_db():
#     db = get_db()

#     with current_app.open_resource('schema.sql') as f:
#         db.executescript(f.read().decode('utf8'))


def init(db):
    db.drop_all()
    db.create_all()

# Il faudrait que tu check les catégories, je les ai pas changé et je sais pas si il faut

                    #  Fruit 

    pomme = Article(nom="Pomme", prix=3, theme=Theme.Alimentaire, 
    categories = Categories.Fruit)
    db.session.add(pomme)

    orange = Article(nom = "Orange", prix=2, theme= Theme.Alimentaire, 
    promotions=1.5,
    categories= Categories.Fruit)
    db.session.add(orange)

    dattes = Article(nom = "Dattes", prix=3.5,  promotions=2.5,
    theme= Theme.Alimentaire, categories=Categories.Fruit)
    db.session.add(dattes)

                        #  Légumes

    poivron = Article(nom = "Poivron", prix=5, 
    theme= Theme.Alimentaire, categories=Categories.Légumes)
    db.session.add(poivron)
    
    oignon = Article(nom = "Oignons", prix=3, 
    theme= Theme.Alimentaire, categories=Categories.Légumes)
    db.session.add(oignon)
    
                    # Spiritueux   

    chivas = Article(nom = "Chivas", prix=30.50,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(chivas)

    greygoose = Article(nom = "Grey Goose", prix=59.50,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(greygoose)

    ricard = Article(nom = "Ricard", prix=23.50,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(ricard)


                    # Softs

    # schewps = Article(nom = "Schweps Agrume", prix=2.70,  
    # theme= Theme.Boissons, categories=Categories.Softs)
    # db.session.add(schewps)
    
    coca = Article(nom = "Coca-Cola Cherry 1L 25", prix=2.70,  
    theme= Theme.Boissons, categories=Categories.Softs)
    db.session.add(coca)

    coca = Article(nom = "Coca-Cola 1L 25", prix=2.70,  
    theme= Theme.Boissons, categories=Categories.Softs)
    db.session.add(coca)

    schewps = Article(nom = "Schweps 1L 25", prix=2.70,  
    theme= Theme.Boissons, categories=Categories.Softs)
    db.session.add(schewps)

    Fanta = Article(nom = "Fanta Orange & Citron 1L 5", prix=2.70,  
    theme= Theme.Boissons, categories=Categories.Softs)
    db.session.add(Fanta)

    Soft50cl = Article(nom = "Boisson 50cl", prix=1.50,  
    theme= Theme.Boissons, categories=Categories.Softs, content= "Sprite & Coca & Coca Cherry & Schweppes & Fanta Orange & Tropico & Schweppes Lemon")
    db.session.add(Soft50cl)

    Soft33cl = Article(nom = "Boisson 33cl", prix=1,  
    theme= Theme.Boissons, categories=Categories.Softs, content= "Oasis Tropical & Ice Tea pêche & 7 UP mojito")
    db.session.add(Soft33cl)


                     # Jus

    # jusorange = Article(nom = "Jus d'Orange", prix=1.70,  
    # theme= Theme.Boissons, categories=Categories.Jus)
    # db.session.add(jusorange)
    
    jusananas = Article(nom = "Jus d'ananas'", prix=2.70,  
    theme= Theme.Boissons, categories=Categories.Jus)
    db.session.add(jusananas)

    juspomme = Article(nom = "Jus de Pomme", prix=2.70,  
    theme= Theme.Boissons, categories=Categories.Softs)
    db.session.add(juspomme)

                      # Café

    nespresso = Article(nom = "Nespresso", prix=3.70,  
    theme= Theme.Boissons, categories=Categories.Café)
    db.session.add(nespresso)

                    #  Thé

    the = Article(nom = "Thé à la Menthe", prix=2.50,  
    theme= Theme.Boissons, categories=Categories.Thé)
    db.session.add(the)
    


                    # Alcool fort 
 
    AlcoolFort = Article(nom = "Vodka Absolut", prix=22.70,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(AlcoolFort)

    AlcoolFort = Article(nom = "Poliakov", prix=17.70,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(AlcoolFort)

    AlcoolFort = Article(nom = "Eristoff", prix=19.20,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(AlcoolFort)

    AlcoolFort = Article(nom = "J&B", prix=19.20,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(AlcoolFort)

    AlcoolFort = Article(nom = "Ricard", prix=19.20,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(AlcoolFort)

    AlcoolFort = Article(nom = "Label 5", prix=17.20,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(AlcoolFort)

    AlcoolFort = Article(nom = "Gin", prix=12,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(AlcoolFort)

    AlcoolFort = Article(nom = "Flash Poliakov", prix=6.50,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(AlcoolFort)

    AlcoolFort = Article(nom = "Flash Label 5", prix=7,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(AlcoolFort)

    AlcoolFort = Article(nom = "Flash Cognac", prix=7.90,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(AlcoolFort)

    AlcoolFort = Article(nom = "Flash Rhum", prix=6.5,  
    theme= Theme.Boissons, categories=Categories.Spiritueux)
    db.session.add(AlcoolFort)

                    # Bières 

    biere = Article(nom = "Heineken 50 cl", prix=2.70,  
    theme= Theme.Boissons, categories=Categories.Bières)
    db.session.add(biere)

    despe = Article(nom = "Desperados 50 cl", prix=2.70,  
    theme= Theme.Boissons, categories=Categories.Bières)
    db.session.add(despe)

    coro = Article(nom = "Corona 50 cl", prix=2.70,  
    theme= Theme.Boissons, categories=Categories.Bières)
    db.session.add(coro)

                    # Vins rouges

    emilton = Article(nom = "Emilton", prix=18.70,  
    theme= Theme.Boissons, categories=Categories.Vins)
    db.session.add(emilton)     
    
    chardonay = Article(nom = "Chardonay", prix=11.10,  
    theme= Theme.Boissons, categories=Categories.Vins)
    db.session.add(chardonay)  
    # db.session.add(Article('fruit', Theme.Alimentaire) )
    # db.session.add(Article("What's your favorite scary movie?", 0))
    
    #  Chips
    pringles = Article(nom = "Pringles Original", prix=3.10,  
    theme= Theme.Alimentaire, categories=Categories.Chips)
    db.session.add(pringles) 

    monster = Article(nom = "Monster", prix=3.30,  
    theme= Theme.Alimentaire, categories=Categories.Chips)
    db.session.add(monster) 

    lays = Article(nom = "Lays", prix=3.20,  
    theme= Theme.Alimentaire, categories=Categories.Chips)
    db.session.add(lays) 

                    # Fromages
    
    boursin = Article(nom = "Boursin", prix=3.70,  
    theme= Theme.Alimentaire, categories=Categories.Fromages)
    db.session.add(boursin) 

    chevre = Article(nom = "Chèvre", prix=4.50,  
    theme= Theme.Alimentaire, categories=Categories.Fromages)
    db.session.add(chevre) 


                    # Charcuterie 
    
    poulethalal = Article(nom = "Blanc Halal de Poulet", prix=3.80,  
    theme= Theme.Alimentaire, categories=Categories.Charcuterie)
    db.session.add(poulethalal)
        
    blanchalal = Article(nom = "Blanc de Dinde Halal", prix=3.90,  
    theme= Theme.Alimentaire, categories=Categories.Charcuterie)
    db.session.add(blanchalal)
                    # Fromages 

    Camembert = Article(nom = "Président Camembert", prix=2.90,  
    theme= Theme.Alimentaire, categories=Categories.Fromages)
    db.session.add(Camembert)

    Emmental = Article(nom = "Emmental Président", prix=2.90,  
    theme= Theme.Alimentaire, categories=Categories.Fromages)
    db.session.add(Emmental)

    Camembert = Article(nom = "Président Camembert", prix=2.90,  
    theme= Theme.Alimentaire, categories=Categories.Fromages)
    db.session.add(Camembert)

                # Produit U.S

    kitkatgld = Article(nom = "KitKat Gold Caramel", prix=1.80,  
    theme= Theme.US, categories=Categories.Gateaux)
    db.session.add(kitkatgld)

    kitkatruby = Article(nom = "KitKat Ruby Chocolate", prix=1.80,  
    theme= Theme.US, categories=Categories.Gateaux)
    db.session.add(kitkatruby)

    kitkatmtcha = Article(nom = "KitKat Green Tea Matcha", prix=1.80,  
    theme= Theme.US, categories=Categories.Gateaux)
    db.session.add(kitkatmtcha)

    ChupaChupsSoda = Article(nom = "Soda Chupa Chups Orange", prix=2.00,  
    theme= Theme.US, categories=Categories.Softs)
    db.session.add(ChupaChupsSoda)

    LionPnt = Article(nom = "Lion Peanut", prix=1.80,  
    theme= Theme.US, categories=Categories.Gateaux)
    db.session.add(LionPnt)

                # Freez

    Freez = Article(nom = "Freez", prix=2,  
    theme= Theme.Alimentaire, categories=Categories.Freez)
    db.session.add(Freez)

    snickers = Article(nom="Snickers Glacé", prix=1.50,
    theme= Theme.Alimentaire, categories= Categories.Freez)
    db.session.add(snickers)

    magnum = Article(nom="Magnum Amandes", prix=2.0,
    theme= Theme.Alimentaire, categories= Categories.Freez)
    db.session.add(magnum)

    
    bounty = Article(nom="Bounty Glacé", prix=1.5,
    theme= Theme.Alimentaire, categories= Categories.Freez)
    db.session.add(magnum)

                # Epi Salées et sucrées

    HotDog = Article(nom = "Hot Dog x2", prix=3.50,  
    theme= Theme.Alimentaire, categories=Categories.Epicerie)
    db.session.add(HotDog)

    Pates = Article(nom = "Pates Panzani", prix=1.80,  
    theme= Theme.Alimentaire, categories=Categories.Epicerie)
    db.session.add(Pates)

    Pesto = Article(nom = "Sauce Pesto", prix=3.00,
    theme= Theme.Alimentaire, categories=Categories.Epicerie)
    db.session.add(Pesto)

    Painmie = Article(nom="Pain de mie",prix=2.5,
    theme= Theme.Alimentaire, categories= Categories.Epicerie)
    db.session.add(Painmie)

    Painprecuit = Article(nom="Pain pré cuit",prix=2.5,
    theme= Theme.Alimentaire, categories= Categories.Epicerie)
    db.session.add(Painprecuit)

    BarChoco = Article(nom="Barres de chocolats diverses", prix=1.00,
    theme= Theme.Alimentaire, categories= Categories.Epicerie, content= "Snickers, Lion, Nuts, KitKat, M&M's, Kinder Bueno, Kinder Bueno white, Twix White, Kinder Delice, Mars")


                    #  Surgelés 

    pizzasaumon = Article(nom="Pizza au Saumon", prix=5.50,
    theme= Theme.Alimentaire, categories= Categories.Surgelés)
    db.session.add(pizzasaumon)


    frites = Article(nom="Frites", prix=3.20,
    theme= Theme.Alimentaire, categories= Categories.Surgelés)
    db.session.add(pizzasaumon)

    nuggets = Article(nom="Nuggets", prix=5.70,
    theme= Theme.Alimentaire, categories= Categories.Surgelés)
    db.session.add(nuggets)

                #  Epicerie

    
    BarChoco = Article(nom="Barres de chocolats diverses", prix=1.00,
    theme= Theme.Alimentaire, categories= Categories.Gateaux, content= "Snickers, Lion, Nuts, KitKat, M&M's, Kinder Bueno, Kinder Bueno white, Twix White, Kinder Delice, Mars")
    db.session.add(BarChoco)

    BarChoco = Article(nom="Makrout aux dattes", prix=2.0,
    theme= Theme.Alimentaire, categories= Categories.Gateaux)
    db.session.add(BarChoco)

    
    tartedaims = Article(nom="Tarte au Daim", prix=2.0,
    theme= Theme.Alimentaire, categories= Categories.Gateaux)

    db.session.add(tartedaims)
   
    db.session.commit()
    
    # db.session.commit()
# def init_db(db):
#     db.drop_all()
#     db.create_all()

#                     #  Fruit 
#     pomme = Article(nom="Pomme", prix=3, theme=Theme.Alimentaire, 
#     categories = Categories.Fruit)
#     db.session.add(pomme)

#     orange = Article(nom = "Orange", prix=2, theme= Theme.Alimentaire, 
#     promotions=1.5,
#     categories= Categories.Fruit)
#     db.session.add(orange)

#     dattes = Article(nom = "Dattes", prix=3.5,  promotions=2.5,
#     theme= Theme.Alimentaire, categories=Categories.Fruit)
#     db.session.add(dattes)

#                         #  Légumes

#     poivron = Article(nom = "Poivron", prix=5, 
#     theme= Theme.Alimentaire, categories=Categories.Légumes)
#     db.session.add(poivron)
    
#     oignon = Article(nom = "Oignons", prix=3, 
#     theme= Theme.Alimentaire, categories=Categories.Légumes)
#     db.session.add(oignon)
    
#                     # Spiritueux   
#     chivas = Article(nom = "Chivas", prix=30.50,  
#     theme= Theme.Boissons, categories=Categories.Spiritueux)
#     db.session.add(chivas)

#     greygoose = Article(nom = "Grey Goose", prix=59.50,  
#     theme= Theme.Boissons, categories=Categories.Spiritueux)
#     db.session.add(greygoose)

#     ricard = Article(nom = "Ricard", prix=23.50,  
#     theme= Theme.Boissons, categories=Categories.Spiritueux)
#     db.session.add(ricard)

#                     # Softs
#     schewps = Article(nom = "Schweps Agrume", prix=2.70,  
#     theme= Theme.Boissons, categories=Categories.Softs)
#     db.session.add(schewps)
    
#     coca = Article(nom = "Coca-Cola Cherry 1L 25", prix=2.70,  
#     theme= Theme.Boissons, categories=Categories.Softs)
#     db.session.add(coca)

#     coca = Article(nom = "Coca-Cola 1L 25", prix=2.70,  
#     theme= Theme.Boissons, categories=Categories.Softs)
#     db.session.add(coca)

#     schewps = Article(nom = "Schweps 1L 25", prix=2.70,  
#     theme= Theme.Boissons, categories=Categories.Softs)
#     db.session.add(schewps)

#                      # Jus

#     jusorange = Article(nom = "Jus d'Orange", prix=1.70,  
#     theme= Theme.Boissons, categories=Categories.Jus)
#     db.session.add(jusorange)
    
#     jusnectar = Article(nom = "Jus de Nectarine", prix=1.30,  
#     theme= Theme.Boissons, categories=Categories.Jus)
#     db.session.add(jusnectar)

#     juspomme = Article(nom = "Jus de Pomme", prix=1.50,  
#     theme= Theme.Boissons, categories=Categories.Softs)
#     db.session.add(juspomme)

#                       # Café

#     nespresso = Article(nom = "Nespresso", prix=3.70,  
#     theme= Theme.Boissons, categories=Categories.Café)
#     db.session.add(nespresso)

#                     #  Thé

#     the = Article(nom = "Thé à la Menthe", prix=2.50,  
#     theme= Theme.Boissons, categories=Categories.Thé)
#     db.session.add(the)
    
#                     # Bières 

#     biere = Article(nom = "Heineken 50 cl", prix=2.70,  
#     theme= Theme.Boissons, categories=Categories.Bières)
#     db.session.add(biere)

#     despe = Article(nom = "Desperados 50 cl", prix=2.70,  
#     theme= Theme.Boissons, categories=Categories.Bières)
#     db.session.add(despe)

#     coro = Article(nom = "Corona 50 cl", prix=2.70,  
#     theme= Theme.Boissons, categories=Categories.Bières)
#     db.session.add(coro)

#                     # Vins rouges

#     emilton = Article(nom = "Emilton", prix=18.70,  
#     theme= Theme.Boissons, categories=Categories.Vins)
#     db.session.add(emilton)     
    
#     chardonay = Article(nom = "Chardonay", prix=11.10,  
#     theme= Theme.Boissons, categories=Categories.Vins)
#     db.session.add(chardonay)  
#     # db.session.add(Article('fruit', Theme.Alimentaire) )
#     # db.session.add(Article("What's your favorite scary movie?", 0))
    
#     #  Chips
#     pringles = Article(nom = "Pringles Original", prix=3.10,  
#     theme= Theme.Alimentaire, categories=Categories.Chips)
#     db.session.add(pringles) 

#     monster = Article(nom = "Monster", prix=3.30,  
#     theme= Theme.Alimentaire, categories=Categories.Chips)
#     db.session.add(monster) 

#     lays = Article(nom = "Lays", prix=3.20,  
#     theme= Theme.Alimentaire, categories=Categories.Chips)
#     db.session.add(lays) 

#                     # Fromages
    
#     boursin = Article(nom = "Boursin", prix=3.70,  
#     theme= Theme.Alimentaire, categories=Categories.Fromages)
#     db.session.add(boursin) 

#     chevre = Article(nom = "Chèvre", prix=4.50,  
#     theme= Theme.Alimentaire, categories=Categories.Fromages)
#     db.session.add(chevre) 
#                     # Charcuterie 
    
#     poulethalal = Article(nom = "Blanc Halal de Poulet", prix=3.50,  
#     theme= Theme.Alimentaire, categories=Categories.Charcuterie)
#     db.session.add(poulethalal)
        
#     blanchalal = Article(nom = "Blanc de Dinde Halal", prix=3.50,  
#     theme= Theme.Alimentaire, categories=Categories.Charcuterie)
#     db.session.add(blanchalal)
#                     # Fromages 

#     db.session.commit()

# init_db(db)
# init_db(db)
    # lg.warning('Database initialized!')
    # db = SQLAlchemy(app)