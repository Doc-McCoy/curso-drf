# Generated by Django 3.0.3 on 2020-02-27 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('core', '0004_pontoturistico_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacao',
            field=models.ManyToManyField(to='avaliacoes.Avaliacao'),
        ),
    ]
