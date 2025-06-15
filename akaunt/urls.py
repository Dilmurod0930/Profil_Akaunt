from  django.urls import path
from  .views import  main,  akaunt_lst

urlpatterns = [
    path('', main, name='main'),
    path('akaunt/', akaunt_lst, name='akaunt_list'),
]