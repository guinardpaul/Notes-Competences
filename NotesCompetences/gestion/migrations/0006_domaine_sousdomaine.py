# Generated by Django 2.0.6 on 2018-06-26 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_auto_20180620_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='domaine',
            name='sousDomaine',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='gestion.Domaine'),
        ),
    ]