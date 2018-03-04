from django.shortcuts import render
from django.http import HttpResponse
import db_connections


def index(request):
    return HttpResponse("yo, nothing here yet, just a placeholder, dont know what to have here yet")

# Just like bottle, this function below does shit and passes dictionary of variables to the html template
# so here i would add the db connectors as we did before
# db_connections is something i made, you can rename it whaevs, im just showing that the py file needs to be in the root directory
# otherwise it won't load

def get_article(request, article_id):
    print(article_id)
    someShit = str(article_id) + ' is a bad number'
    return render(request, 'article/article.html', {'id' : article_id, 'someShit':someShit})
