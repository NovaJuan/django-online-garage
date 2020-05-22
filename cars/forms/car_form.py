from django import forms


class CarForm(forms.Form):
    name = forms.CharField(label='Car name', max_length=100, required=True)
