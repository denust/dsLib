import psycopg2
import pandas as pd
import getpass
from time import strftime

def connect_to_db():
    username = input('State your name cuz ')
    password = getpass.getpass('What we doing today? ')
    conn = psycopg2.connect(f"dbname=duck \
                        user = {username} \
                        password = {password} \
                        host = duckdb.ccyc8kurysq2.us-east-2.rds.amazonaws.com")
    cursor = conn.cursor()
    return cursor, conn

#cursor,conn = connect_to_db()

# Need to add primary keys and autoincrementing shit later maybe
def make_articles_table(cursor, conn):
    query = """CREATE TABLE articles_all (
    article_id varchar(255),
    article_body text,
    upload_date varchar(255),
    author varchar(255)
    );"""
    cursor.execute(query)
    conn.commit()


def drop_articles_table(cursor, conn):
    query = """DROP TABLE articles_all"""
    cursor.execute(query)
    conn.commit()


def show_tables(cursor, conn):
    query = """SELECT table_catalog,table_schema,table_name,table_type
    FROM INFORMATION_SCHEMA.TABLES WHERE table_schema='public'"""
    cursor.execute(query)
    results = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    conn.commit()
    return pd.DataFrame(data=results, columns=colnames)


def add_article(cursor, conn, article_id, article_body, author):
    upload_date = strftime("%d/%m/%y %H:%M:%S")
    # replacing ' with `, need better solution
    values = tuple([article_id, article_body.replace("'", "`"), upload_date, author])
    query = f"""INSERT INTO articles_all VALUES {values}"""
    cursor.execute(query)
    conn.commit()


def find_article(cursor, conn, article_id):
    query = f"""SELECT * FROM articles_all where article_id = '{article_id}'"""
    cursor.execute(query)
    conn.commit()
    result = cursor.fetchall()
    if len(result) == 0:
        return ['', 'nah nuthin ere m8']
    else:
        return result[0]



