from django.http import HttpResponse

def index(request):
    return HttpResponse("Just go to articles/{number}")