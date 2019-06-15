from django import forms

class Enquary(forms.Form):
    name=forms.CharField(max_length=200)
    