# Generated by Django 2.0.6 on 2018-06-26 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_auto_20180626_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='classe',
        ),
    ]