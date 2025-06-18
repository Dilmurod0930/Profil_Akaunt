from django.urls import path
from  .views import  main, profil_lst, profil_add, profil_update

urlpatterns = [
    path('', main, name='main'),
    path('profil_lst/', profil_lst, name='profil_lst'),
    path('profil_add/', profil_add, name='profil_add'),
    path('profil_update/<int:id>', profil_update, name='profil_update'),
]