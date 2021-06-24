from django import forms
from .models import Atraccion


class CrearForm(forms.ModelForm):
    class Meta:
        model = Atraccion
        fields = "__all__"
