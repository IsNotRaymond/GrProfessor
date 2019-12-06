from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Turma(models.Model):
    user = models.ForeignKey(User,
                             editable=False,
                             null=False,
                             blank=False,
                             on_delete=models.CASCADE)

    nome_turma = models.CharField(max_length=100,
                                  null=False,
                                  blank=False,
                                  verbose_name='Nome da turma',
                                  help_text='Use um nome significativo',
                                  unique=True)

    data_criacao = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.nome_turma
