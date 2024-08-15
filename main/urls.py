from django.urls import path
from. import views
from django.conf.urls.static import static
from django.conf import settings

app_name= "main"


""""
'i' joue le meme role que le variable 'use' mais il est utiluser seulement pour les message
am'ty magnaboaka lien n historique n mesg

    path('msg/', views.msg, name="msg"),#liste na message

"""
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:use_id>/', views.voir, name="voir"),
    path('msg/', views.msg, name="msg"),
    path('<int:i_id>/', views.msg2, name="msg2"),
    
    path('publier/', views.pub, name='pub'),
    #path('<int:user_id>/', views.description, name="description")

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
