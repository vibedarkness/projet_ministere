# Generated by Django 4.1.3 on 2022-12-04 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BordereauAdministratif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parametre', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('numero_ordre', models.IntegerField()),
                ('type_echantillon', models.CharField(max_length=500)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.client')),
            ],
        ),
        migrations.RemoveField(
            model_name='facture',
            name='prix_total',
        ),
        migrations.AlterField(
            model_name='facture',
            name='designation',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Attestation',
        ),
    ]
