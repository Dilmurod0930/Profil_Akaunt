from django.urls import path
from  .views import  main, profil_lst

urlpatterns = [
    path('', main, name='main'),
    path('profil_lst/', profil_lst, name='profil_lst'),
]