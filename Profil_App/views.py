from django.shortcuts import render, redirect, get_object_or_404

from .forms import Profil_Form
from .models import  Profil_Model

# Create your views here.
def  main(request):
    return render(request, 'main.html')

def  profil_lst(request):
    akaunt = Profil_Model.objects.all()
    context = {'akaunt': akaunt}
    return render(request, 'akaunt/akaunt_lst.html', context = context)


def profil_add(request):
    form = Profil_Form(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('profil_lst')
    return render(request, 'akaunt/akaunt_add.html', {'form': form})