# Generated by Django 2.2.7 on 2019-12-17 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grupo', '0001_initial'),
        ('Aluno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='grupo_pertencente',
            field=models.ManyToManyField(to='Grupo.Grupo'),
        ),
    ]
