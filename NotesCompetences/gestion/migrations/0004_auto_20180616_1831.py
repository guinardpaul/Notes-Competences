# Generated by Django 2.1 on 2018-06-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20180616_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competence',
            name='ref',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='domaine',
            name='ref',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]