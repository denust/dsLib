from django.shortcuts import render
from django.http import HttpResponse
from db_connections import *


def index(request):
    return HttpResponse("yo, nothing here yet, just a placeholder, dont know what to have here yet")

# Just like bottle, this function below does shit and passes dictionary of variables to the html template
# so here i would add the db connectors as we did before
# db_connections is something i made, you can rename it whaevs, im just showing that the py file needs to be in the root directory
# otherwise it won't load

def get_article(request, article_id):
    article = find_article(cursor,conn,article_id)
    article_body = article[1].replace(r'\n', '<br>')
    try:
        upload_date = article[2]
        author = article[3]
    except:
        upload_date = 'not yet'
        author = 'no one'
    return render(request, 'article/article.html', {'id' : article_id, 'article_body' :article_body, 'upload_date': upload_date,
                                                    'author':author} )
