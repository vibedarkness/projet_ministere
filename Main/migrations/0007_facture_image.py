# Generated by Django 4.1.4 on 2023-01-01 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_remove_bordereauadministratif_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture',
            name='image',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
    ]
