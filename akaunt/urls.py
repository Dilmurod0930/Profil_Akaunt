from  django.urls import path
from  .views import  main,  akaunt_lst,  akaunt_add

urlpatterns = [
    path('', main, name='main'),
    path('akaunt/', akaunt_lst, name='akaunt_lst'),
    path('akaunt-add/', akaunt_add, name='akaunt-add'),
]