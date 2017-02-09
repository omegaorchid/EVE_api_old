from django import forms
from .models import Join


class Register(forms.ModelForm):

    class Meta:
        model = Join
        fields = ('first_name', 'email')
