from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1 style="text-align: center">Hello Word</h1>')
