# Generated by Django 2.2.7 on 2019-12-18 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turma', '0006_auto_20191216_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='data_criacao',
            field=models.DateField(default='2019-12-18'),
        ),
    ]
