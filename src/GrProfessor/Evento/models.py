from django.db import models
from ..Turma.models import Turma


class Evento(models.Model):
    turma_pertencente = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE)
    nome_evento = models.CharField(max_length=200, null=False, blank=False)
    descricao_evento = models.TextField()
    quantidade_atividades = models.IntegerField(null=False, blank=False)
