# from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from datetime import timedelta
import enum

from flask import Flask,render_template,url_for,request, g, session,logging,redirect,flash, url_for, Blueprint


from sqlalchemy.orm import scoped_session,sessionmaker
from passlib.hash import sha256_crypt

# from models import * 
# import models
# from init_db import init_db

# from models import User, Todo, Blogpost, Channel, Article

# all_views = Blueprint("all_views", __name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vitrine.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.register_blueprint(models, url_prefix="")
app.permanent_session_lifetime = timedelta(days=5)

db = SQLAlchemy(app)


# from models import *

from init_db import *



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

@app.route('/articles', methods=['GET', 'POST'])
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

@app.route('/categories', methods=["GET", 'POST'])
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

                #   New Post


@app.route('/articles/new', methods=['GET', 'POST'])
def new_art():
    if request.method == 'POST':
        post_title = request.form['title']
        # if session['User'] == True:
        #    post_author = session['Username']
        # else:
        #    post_author = request.form['author']
        post_author = request.form['author']
        post_content = request.form['content']
        new_post = Article(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('new_post.html')

                    #  User creation
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form.get("name")
        username=request.form.get("Username")
        password=request.form.get("password")
        confirm=request.form.get("confirm")
        secure_password=sha256_crypt.encrypt(str(password))
        
        usernamedata = User.query.filter_by(username=username)
        usernamedata=str(usernamedata)
        if usernamedata==None:
            if password==confirm:
                 new_User = User(login=username, name=name, password=secure_password)
                 db.session.add(new_User)
                 db.session.commit()
                 flash("You are registered and can now login","success")
                 return redirect(url_for('login'))
            else:
                flash("password does not match","danger")
                return render_template('register.html')
        else :
            flash("User already existed, please login or contact admin","danger")
            return redirect(url_for('login'))
 
    return render_template('register.html')
 
                                        #  User login


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        Username=request.form.get("name")
        password=request.form.get("password")
 
        usernamedata=db.Query("SELECT Username FROM Users WHERE Username=:Username",{"Username":Username}).fetchone()
        passworddata=db.Query("SELECT password FROM Users WHERE Username=:Username",{"Username":Username}).fetchone()
        usernamedata = User.query.filter_by(Username=Username)
 
        if usernamedata is None:
            flash("No Username","danger")
            return render_template('login.html')
        else:
            for passwor_data in passworddata:
                if sha256_crypt.verify(password,passwor_data):
                    session["log"]=True
                    User = request.form["nm"]
                    session.permanent = True
                    session['User'] = User
                    flash("You are now logged in!!","success")
                    return redirect(url_for('todo')) #to be edited from here do redict to either svm or home
                else:
                    flash("incorrect password","danger")
                    return render_template('login.html')
 
    return render_template('login.html')



                                # Todo listing

@app.route("/todo/", methods=['POST', 'GET'])
def todo_new():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/todo')
        except:
            return 'There was an issue adding your task'

    else :
        # tasks = db.Query("SELECT * FROM Todo ").fetchone()
        tasks = Todo.query.order_by(Todo.date_created).all()
        if tasks is None :
            return render_template('Todo.html')
        else:
            return render_template('Todo.html', tasks=tasks)

                                # Todo delete

@app.route('/todo/delete/<int:id>')
def delete_Todo(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/todo/')
    except:
        return 'There was a problem deleting that task'

                                # Todo  update

@app.route('/todo/update/<int:id>', methods=['GET', 'POST'])
def update_Todo(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/todo/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)

if __name__ == "__main__":

    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    init(db)
    # app.debug = True
    app.run()


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

