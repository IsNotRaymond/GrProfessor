from django import forms
from .models import Atividade


class DateInput(forms.DateInput):
    input_type = 'date'


class AtividadeForm(forms.ModelForm):
    data_atividade = forms.DateField(widget=DateInput)

    class Meta:
        model = Atividade

        fields = ('nome_atividade', 'descricao_atividade', 'data_atividade')
