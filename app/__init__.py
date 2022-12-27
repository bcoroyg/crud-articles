from flask import Flask, redirect, url_for, render_template, request

import database

from flask_bootstrap import Bootstrap5

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/articles')
def get_articles():
    articles = database.list_articles()
    return render_template('article/index.html', articles=articles)


@app.route('/articles/add', methods=["GET", "POST"])
def create_article():
    if request.method == "POST":
        name = request.form['name']
        price = request.form['price']

        database.insert_article(name, price)

        return redirect(url_for("get_articles"))

    return render_template("article/add.html")


@app.route("/article/<int:id>/edit", methods=["GET", "POST"])
def update_article(id):

    if request.method == "POST":
        name = request.form['name']
        price = request.form['price']

        database.update_article(id, name, price)

        return redirect(url_for("get_articles"))

    article = database.get_article(id)
    return render_template('article/edit.html', article=article)


@app.route("/article/delete", methods=["POST"])
def delete_article():
    id = request.form['id']
    database.delete_article(id)
    return redirect(url_for("get_articles"))


def create_app():
    Bootstrap5(app)
    return app
