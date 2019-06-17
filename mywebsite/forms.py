from django import forms
from .models import personM



class personMForm(forms.ModelForm):

    class Meta:
        model = personM
        fields = [
            'f_name',
            'l_name',
            'email',
            'phone_num'
        ]