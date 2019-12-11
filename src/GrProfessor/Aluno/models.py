from django.db import models
from ..Turma.models import Turma


class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=200,
                                  null=False,
                                  blank=False,
                                  verbose_name='Nome do aluno',
                                  help_text="Nome para identificação do aluno")

    turma_pertencente = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_aluno
