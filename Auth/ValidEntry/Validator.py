from django import forms
class PersonneValid(forms.Form):
    nom = forms.CharField(max_length=20)
    prenom = forms.CharField(max_length=20)
    datedenaisse = forms.DateField
    username = forms.CharField(max_length=20)
    # Professor
    email = forms.EmailField(max_length=40)
    password = forms.CharField(max_length=20)
    confirmpassword =  forms.CharField(max_length=20)