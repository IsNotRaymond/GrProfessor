from django.db import models
from ..Turma.models import Turma
from ..Aluno.models import Aluno
from ..Grupo.models import Grupo


class Atividade(models.Model):
    turma_pertencente = models.ForeignKey(Turma, null=False, blank=False, on_delete=models.CASCADE)

    nome_atividade = models.CharField(max_length=200,
                                      null=False,
                                      blank=False,
                                      verbose_name='Nome da atividade',
                                      help_text='Apenas um nome para identificação')

    descricao_atividade = models.TextField(verbose_name='Descrição da Atividade')

    data_atividade = models.DateField()

    grupo_atribuido = models.ForeignKey(Grupo, null=True, blank=True, on_delete=models.SET_NULL)

    aluno_atribuido = models.ForeignKey(Aluno, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome_atividade
