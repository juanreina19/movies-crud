from django.forms import ModelForm
from django import forms
from .models import *

class MovieForm(ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'
        exclude = ['id']
        widgets = { 'fecha': forms.DateInput(attrs={'type': 'date'})}
        labels = {'id_director': 'Director'}

class SocioForm(ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'
        exclude = ['id', 'user']

class CodeudorForm(ModelForm):
    class Meta:
        model = Codeudor
        fields = ['id_codeudor']
        labels = {'id_codeudor': 'Cosigner'}
        widgets = {'id_codeudor': forms.Select(attrs={'class': 'select-input'})}

    def __init__(self, *args, **kwargs):
        # Obtener el socio autenticado (se pasa por kwargs)
        socio = kwargs.pop('socio', None)
        super(CodeudorForm, self).__init__(*args, **kwargs)
        
        # Filtrar para que no se muestre el socio actual como una opción en id_codeudor
        if socio:
            self.fields['id_codeudor'].queryset = Socio.objects.exclude(id=socio.id)


class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = ['fecha_alquiler', 'fecha_devolucion']  # No incluye as_delivered
        widgets = {
            'fecha_alquiler': forms.HiddenInput(),
            'fecha_devolucion': forms.HiddenInput()
        }