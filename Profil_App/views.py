from django.shortcuts import render
from .models import  Profil_Model

# Create your views here.
def  main(request):
    return render(request, 'main.html')

def  profil_lst(request):
    akaunt = Profil_Model.objects.all()
    context = {'akaunt': akaunt}
    return render(request, 'akaunt/akaunt_lst.html', context = context)