from enum import unique
from django import forms

class SendTextForm(forms.Form):
    text = forms.CharField(label="Text", max_length=1000)


class AuthAndLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
