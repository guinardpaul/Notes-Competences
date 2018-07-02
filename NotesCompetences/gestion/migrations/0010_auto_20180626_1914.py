# Generated by Django 2.0.6 on 2018-06-26 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0009_eleve_classe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaine',
            name='sous_domaine',
            field=models.ForeignKey(blank=True, default=-1, on_delete=django.db.models.deletion.CASCADE, to='gestion.Domaine'),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='classe',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='gestion.Classe'),
        ),
    ]
