# Generated by Django 2.0.6 on 2018-07-11 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0017_auto_20180704_1831'),
        ('resultat', '0002_auto_20180704_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='classe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gestion.Classe'),
            preserve_default=False,
        ),
    ]