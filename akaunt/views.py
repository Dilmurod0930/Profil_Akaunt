from django.shortcuts import render
from  .models import  Profile

# Create your views here.

def  main(request):
    return render(request, 'main.html')

def  akaunt_lst(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'akaunt/akaunt_list.html', context = context )