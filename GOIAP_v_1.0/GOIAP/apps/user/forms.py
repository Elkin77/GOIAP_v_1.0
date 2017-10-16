from django import forms

class login_form(forms.Form):
    user=forms.CharField()
    password=forms.CharField()