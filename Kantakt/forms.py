from    django import forms

class  ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)

    def  clean_name(self):
        name =  self.cleaned_data['name']
        if  len(name) < 3:
            raise  forms.ValidationError("Name must be at least 3 characters long")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if  email  in  "@gmail.com":
            raise forms.ValidationError("Email must be at least 1 character")
        return email

    def  clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 40:
            raise forms.ValidationError("Message must be at least 40 characters long")
        return message
    