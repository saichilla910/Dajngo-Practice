from django import forms
from .models import Profile
class profile_Form(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'