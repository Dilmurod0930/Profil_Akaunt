from django.shortcuts import render, redirect

from Profil_Prayekt.Kantakt.forms import ContactForm


# Create your views here.
def  contact_form(request):
    form  =  ContactForm(request.POST , request.FILES)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        phone_number = form.cleaned_data['phone_number']
        print(F"Name: {name} \nEmail: {email} \nPhone_Number: {phone_number} \n  Message: {message}")
        return redirect('main')
    return render(request,'contact/contact_form.html',{'form':form})
