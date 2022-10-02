# listings/forms.py

from django import forms
class submitForm(forms.Form):
   lon1 = forms.CharField(max_length=10)
   lat1 = forms.CharField(max_length=10)