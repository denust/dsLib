from django.shortcuts import render
from django.http import HttpResponse
from db_connections import *


# Importing markdown stuff
from article.forms import MyForm



def index(request):
    return HttpResponse("yo, nothing here yet, just a placeholder, dont know what to have here yet")


def get_article(request, article_id):

    article_body = '# Today we will be playing'

    form_class = MyForm 

    try:
        upload_date = 'today'#article[2]
        author = 'den'#article[3]
    except:
        upload_date = 'not yet'
        author = 'no one'
    return render(request, 'article/article.html', {'id' : article_id, 'article_body' :article_body, 'upload_date': upload_date,
                                                    'author':author, 'form': form_class} )
