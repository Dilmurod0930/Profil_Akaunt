from django.urls import path
from  .views import  main, profil_lst, profil_add, profil_update, profil_del

urlpatterns = [
    path('', main, name='main'),
    path('profil_lst/', profil_lst, name='profil_lst'),
    path('profil_add/', profil_add, name='profil_add'),
    path('profil_update/<int:id>', profil_update, name='profil_update'),
    path('profil_del/<int:id>', profil_del, name='profil_del'),
]