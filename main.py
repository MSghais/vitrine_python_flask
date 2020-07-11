from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from datetime import timedelta
import enum

from flask import Flask,render_template,url_for,request, g, session,logging,redirect,flash, url_for, Blueprint


app = Flask(__name__)

app.permanent_session_lifetime = timedelta(days=5)


db = SQLAlchemy(app)
from models import *



ENV = "prod"

if ENV == "dev":
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vitrine.db'

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ebbuzrqxzvdndv:1f2603a168ff4526e5b80b72905a47bc4d1a5d390e5ed3611437f88631c2c6b0@ec2-34-197-141-7.compute-1.amazonaws.com:5432/d9btjknhvpqhe9"


# db = SQLAlchemy(app)

# # db.create_all()

from init_db import init


# init(db)

# from models import *


         ##Routing all

@app.route('/')
def index():
    return render_template('index.html')

#   Posting

@app.route('/contact', methods=['GET', 'POST'])
def contact():
        return render_template('contact.html')
    
@app.route('/promotions/')
def promotions():
    articles = Article.query.order_by(Article.date_posted).all()
    articles_promo = []
    for article in articles:
        if article.promotions != None:
            articles_promo.append(article)
    print(articles_promo)
    # return render_template('promotions.html', articles=articles_promo )
    return render_template('promotions.html', articles=articles)

#  View article 
@app.route('/article/<int:id>/')
def article_view(id):
        categories = list(Categories)
        themes = list(Theme)
        article = Article.query.filter_by(id= id).first()
        return render_template('article.html', article=article, categories=categories, themes=themes)

            #    Tout les Articles et recherche sous catégories

@app.route('/articles/', methods=['GET', 'POST'])
def articles_tous():

    if request.method == 'POST':
        categories = list(Categories)
        themes = list(Theme)
        if request.form.get("research") == "research":
            categ_name = request.form['categorie']
            print(categ_name)
      
            arti = Article.query.filter_by(categories= categ_name).all()
            print(arti)
            return render_template('tout_articles.html', themes=themes, 
            categories= categories, categ_name = categ_name , articles=arti)
        elif request.form.get("deselect") == "deselect":
            articles = Article.query.order_by(Article.categories).all()
            categories = list(Categories)
            themes = list(Theme)
            return render_template('tout_articles.html', articles=articles,
             categories=categories
            ,themes= themes)
        elif request.form.get("deselection") == "Tout nos produits" :
            categories = list(Categories)
            themes = list(Theme)
            arti = Article.query.order_by(Article.theme).all()
            return render_template('tout_articles.html', themes=themes,
            categories= categories, articles=arti)
    else:
        articles = Article.query.order_by(Article.categories).all()
        categories = list(Categories)
        themes = list(Theme)
        return render_template('tout_articles.html', articles=articles, categories=categories
        ,themes= themes)

                        # Categories et recherche

@app.route('/categories/', methods=["GET", 'POST'])
def categories():
    if request.method == 'POST':
        if request.form.get("research") == "research":
            categories = list(Categories)
            themes = list(Theme)
            theme_name = request.form['categorie']
            print(theme_name)
            arti = Article.query.filter_by(theme= theme_name).all()
            return render_template('categories.html', themes=themes,
            categ= categories, theme_name = theme_name , articles=arti)
        elif request.form.get("deselection") :
            categories = list(Categories)
            themes = list(Theme)
            arti = Article.query.order_by(Article.theme).all()
            return render_template('categories.html', themes=themes,
            categ= categories, articles=arti)
        elif request.form.get("deselect") == "deselect":
            categories = list(Categories)
            themes = list(Theme)
            arti = Article.query.order_by(Article.theme).all()
            return render_template('categories.html', themes=themes,
            categ= categories, articles=arti)
    else:
        categories = list(Categories)
        themes = list(Theme)
        arti = Article.query.order_by(Article.theme).all()
        return render_template('categories.html', themes =  themes , 
        categ=categories, articles=arti)


                    #  Recherche
@app.route('/recherche', methods=['GET', 'POST'])
def articles_search():
    categories = list(Categories)
    themes = list(Theme)
    arti = Article.query.order_by(Article.categories).all()
    return render_template('recherche.html', themes=themes,
    categories= categories, articles=arti)

    if request.method == 'POST':
        
        categories = list(Categories)
        themes = list(Theme)
        arti = Article.query.order_by(Article.categories).all()
        return render_template('recherche.html', themes=themes,
        categories= categories, articles=arti)
    else:
        categories = list(Categories)
        themes = list(Theme)
#   Delete Post

@app.route('/articles/delete/<int:id>')
def art_delete(id):
    post = Article.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

                #   Edit Post

@app.route('/articles/edit/<int:id>', methods=['GET', 'POST'])
def art_edit(id):
    
    post = Article.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=post)




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

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vitrine.db'
    # app.secret_key = 'super secret key'
    # app.config['SESSION_TYPE'] = 'filesystem'

            
    ENV = "prod"

    if ENV == "dev":
        app.debug = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vitrine.db'

    else:
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ebbuzrqxzvdndv:1f2603a168ff4526e5b80b72905a47bc4d1a5d390e5ed3611437f88631c2c6b0@ec2-34-197-141-7.compute-1.amazonaws.com:5432/d9btjknhvpqhe9"


    init(db)

    app.run()

    # init(db)
    # app.debug = True
    # app.run()

    
# ## Others Login

# @app.route("/login",methods=["GET","POST"])
# def logintest():
#     if request.method == 'POST':
#         session.pop('User', None)

#         if request.form['password'] == 'password':
#             session['User'] = request.form['Username']
#             return redirect(url_for('protected'))

#     return render_template('login.html')
 
 
# @app.route("/protected",methods=["GET","POST"])
# def protected():
#     if g.User:
#         return render_template('protected.html', User= session['User'])

#     return redirect(url_for('login'))

# @app.before_request
# def before_request():
#     g.User = None
#     if 'User' in session:
#         g.User = session['User']


# @app.route('/disconnect')
# def disconnect():
#     session.pop('User', None)
#     return render_template('login.html')

