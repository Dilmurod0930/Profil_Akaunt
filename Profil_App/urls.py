from django.urls import path
from  .views import  main, profil_lst, profil_add

urlpatterns = [
    path('', main, name='main'),
    path('profil_lst/', profil_lst, name='profil_lst'),
    path('profil_add/', profil_add, name='profil_add'),
]