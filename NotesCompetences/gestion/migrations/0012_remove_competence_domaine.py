# Generated by Django 2.0.6 on 2018-06-26 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0011_auto_20180626_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competence',
            name='domaine',
        ),
    ]
