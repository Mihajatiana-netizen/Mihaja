from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'acceuil/index.html')
# Create your views here.
