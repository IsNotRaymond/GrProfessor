from django.db import models


class Evento(models.Model):

    nome_evento = models.CharField(max_length=200, null=False, blank=False)