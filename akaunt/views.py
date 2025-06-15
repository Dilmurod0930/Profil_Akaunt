from django.shortcuts import render

# Create your views here.

def  main(request):
    return render(request, 'main.html')

def  akaunt_lst(request):
    return render(request, 'akaunt/akaunt_list.html' )