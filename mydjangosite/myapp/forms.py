from django import forms
from .models import Result
import calculation

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["name","maths","english","science","average"]


    widgets = {
    'grade': calculation.FormulaInput(('maths' + 'english' + 'science'))
       }





