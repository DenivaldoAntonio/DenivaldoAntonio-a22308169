
from django import forms

from .models import (
    UnidadeCurricular,
    Docente
)


class UnidadeCurricularForm(forms.ModelForm):

    class Meta:

        model = UnidadeCurricular

        fields = '__all__'


class DocenteForm(forms.ModelForm):

    class Meta:

        model = Docente

        fields = '__all__'