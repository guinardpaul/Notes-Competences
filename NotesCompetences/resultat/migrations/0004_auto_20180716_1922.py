# Generated by Django 2.0.6 on 2018-07-16 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resultat', '0003_evaluation_classe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='classe',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='competence',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='cycle',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='trimestre',
        ),
        migrations.AlterField(
            model_name='resultat',
            name='evaluation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Evaluation'),
        ),
        migrations.DeleteModel(
            name='EnumTrimestre',
        ),
        migrations.DeleteModel(
            name='Evaluation',
        ),
    ]