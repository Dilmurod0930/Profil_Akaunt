from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProfileForm
from  .models import  Profile

# Create your views here.

def  main(request):
    return render(request, 'main.html')

def  akaunt_lst(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'akaunt/akaunt_lst.html', context = context )

def akaunt_add(request):
    form  =  ProfileForm(request.POST , request.FILES )
    if form.is_valid():
        form.save()
        return redirect('akaunt_lst')
    return render(request, 'akaunt/akaunt_add.html' , {'form':form})
