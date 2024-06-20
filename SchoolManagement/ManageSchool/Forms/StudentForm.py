# forms.py

from django import forms
from ..ModelsOfDatabase.StudentDataModel import Studentdatamodel


class StudentForm(forms.Form):
    parentmobile = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Studentdatamodel
        fields = ['parentmobile', 'password']
