from django import forms

class SendTextForm(forms.Form):
    text = forms.CharField(label="Text", max_length=1000)
