# Generated by Django 2.1 on 2019-09-18 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pantalla',
            name='Piso',
            field=models.CharField(choices=[('PB', 'BAJA'), ('P1', 'UNO'), ('P2', 'DOS')], default='PB', max_length=2),
        ),
    ]
