# Generated by Django 4.1.4 on 2022-12-27 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_facture_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facture',
            name='user',
        ),
    ]
