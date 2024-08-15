from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profil, Publication, Commentaires, Message
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from .forms import PubForm

#Gestio des messages
def index(request):
    users= User.objects.all()
    profil= Profil.objects.all()   
    pb= Publication.objects.all().order_by("-profil")   
    coms= Commentaires.objects.all()

    context= {
        'users':users,
        'profil':profil,
        'pb':pb,
        'coms':coms

    }
    return render (request, 'main/index.html', context)

# voir profil

def voir(request, use_id):
    context = {"use" : get_object_or_404(User, pk= use_id)}
    return render(request, "main/voir.html", context)

# gestion de message
def msg(request):
    users= User.objects.all()
    context= {'users':users}
    return render (request, 'main/msg.html', context)


def msg2(request, user_id):
    context = {"user" : get_object_or_404(User, pk= user_id)} 
    return render(request, "main/msg2.html", context)

""""
#gestion de publication
    #"puble" aganran fichier html missy formulaire io

"""
def pub(request):
    if request.method == 'POST':
        form =PubForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("main:index")
    else:
        form = PubForm()
    return render(request, "main/pub.html", {"form": form})


def descriptions():
    pass