from django.forms import ModelForm
from .models import Evento


class EventoForm(ModelForm):

    class Meta:
        model = Evento
        fields = ('nome_evento', 'descricao_evento', 'quantidade_atividades', )
