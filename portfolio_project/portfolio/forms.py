
from django import forms

from .models import (
    UnidadeCurricular,
    Docente,
    Tecnologia
)


class UnidadeCurricularForm(forms.ModelForm):

    class Meta:

        model = UnidadeCurricular

        fields = '__all__'


class DocenteForm(forms.ModelForm):

    class Meta:

        model = Docente

        fields = '__all__'

class TecnologiaForm(forms.ModelForm):

    class Meta:

        model = Tecnologia

        fields = '__all__'