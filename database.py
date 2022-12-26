import pymysql
from config import config

cfg = config['development']

config = {
    "user": cfg.MYSQL_USER,
    "password": cfg.MYSQL_PASSWORD,
    "host": cfg.MYSQL_HOST,
    "db": cfg.MYSQL_DB,
    "port": cfg.MYSQL_PORT
}


def connectdb():
    # return pymysql.connect(
    #     host=cfg.MYSQL_HOST,,
    #     user=cfg.MYSQL_USER,
    #     password=cfg.MYSQL_PASSWORD,
    #     db=cfg.MYSQL_DB,
    #     port=cfg.MYSQL_PORT
    # )
    return pymysql.connect(**config)


def insert_article(name, price):
    conect = connectdb()
    with conect.cursor() as cursor:
        cursor.execute("INSERT INTO article(name, price) VALUES (%s, %s)", (name, price))
        conect.commit()
        conect.close()

def list_articles():
    connect = connectdb()
    articles = []
    with connect.cursor() as cursor:
        cursor.execute("SELECT id, name, price FROM article")
        articles = cursor.fetchall()
        connect.close()
        return articles

def delete_article(id):
    connect = connectdb()
    with connect.cursor() as cursor:
        cursor.execute("DELETE FROM article WHERE id = %s", (id))
        connect.commit()
        connect.close()

def get_article(id):
    connect = connectdb()
    article = None
    with connect.cursor() as cursor:
        cursor.execute("SELECT id, name, price FROM article WHERE id = %s", (id))
        article = cursor.fetchone()
        connect.close()
        return article

def update_article(id, name, price):
    connect= connectdb()
    with connect.cursor() as cursor:
        cursor.execute("UPDATE article SET name = %s, price=%s WHERE id = %s", (name, price, id))
        connect.commit()
        connect.close()

#if __name__ == '__main__':
    #print(list_articles())
