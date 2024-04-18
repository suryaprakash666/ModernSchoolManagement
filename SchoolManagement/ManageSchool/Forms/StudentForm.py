# forms.py

from django import forms
from ..models import Studentdatamodel


class StudentForm(forms.ModelForm):
    class Meta:
        model = Studentdatamodel
        fields = ['Student_Firstname', 'Student_Password']  # Add more fields as needed


