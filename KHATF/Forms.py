from django import forms


class CLasses(forms.Form):
    name = forms.CharField(max_length=100)
    file = forms.FileField()
