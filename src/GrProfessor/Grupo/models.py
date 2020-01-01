from django.db import models
from django.utils import timezone


class Grupo(models.Model):
    nome_grupo = models.CharField(max_length=100,
                                  null=False,
                                  blank=False,
                                  verbose_name='Nome do grupo',
                                  help_text='Use um nome significativo')

    data_criacao = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.nome_grupo

