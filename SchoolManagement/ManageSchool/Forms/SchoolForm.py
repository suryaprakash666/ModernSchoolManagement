# forms.py

from django import forms
from ..models import Schooldatamodel


class SchoolForm(forms.ModelForm):
    class Meta:
        model = Schooldatamodel
        fields = ['School_Name', 'School_Key']
        # Add more fields as needed
