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




def  profil_update(request,  id):
    profil  =  get_object_or_404(Profil_Model, id=id)
    form  = Profil_Form(request.POST or None , request.FILES, instance= profil )
    if form.is_valid():
        form.save()
        return redirect('profil_lst', id = id)
    return render(request, 'akaunt/akaunt_update.html', {'form': form})


def  profil_del(request, id):
    profil = get_object_or_404(Profil_Model, id=id)
    if  request.method == 'POST':
        profil.delete()
        return redirect('profil_lst')
    return render(request, 'akaunt/akaunt_del.html', {'profil': profil})
