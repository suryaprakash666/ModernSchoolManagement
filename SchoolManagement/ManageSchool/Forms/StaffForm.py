# forms.py

from django import forms
from ..ModelsOfDatabase.StaffDataModel import Staffdatamodel


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staffdatamodel
        fields = ['name', 'password']
