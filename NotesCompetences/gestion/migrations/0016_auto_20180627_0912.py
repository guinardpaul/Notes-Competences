# Generated by Django 2.0.6 on 2018-06-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0015_auto_20180626_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competence',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='domaine',
            name='description',
            field=models.TextField(),
        ),
    ]
