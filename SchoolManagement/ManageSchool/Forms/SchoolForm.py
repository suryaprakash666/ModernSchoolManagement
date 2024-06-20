# forms.py

from django import forms
from ..ModelsOfDatabase.SchoolDataModel import Schooldatamodel


class SchoolForm(forms.Form):
    email = forms.EmailField()
    passkey = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Schooldatamodel
        fields = ['email', 'passkey']
