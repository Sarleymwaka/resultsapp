from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['name','english','math','science','grade']


