# Generated by Django 3.0 on 2020-01-10 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_control_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlCompleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdControl', models.CharField(max_length=20)),
                ('EstadoP', models.CharField(choices=[('Encender', '1'), ('Apagar', '2'), ('Error', '0')], default='Error', max_length=8)),
                ('EstadoT', models.CharField(choices=[('Encender', '1'), ('Apagar', '2'), ('Error', '0')], default='Error', max_length=8)),
                ('Mute', models.CharField(choices=[('Encendido', '1'), ('Apagado', '0')], default='Encendido', max_length=10)),
                ('Vol', models.CharField(choices=[('25%', 'V1'), ('50%', 'V2'), ('75%', 'V3')], default='25%', max_length=4)),
                ('IP', models.CharField(default='0.0.0.0', max_length=16)),
                ('IdPantalla', models.CharField(max_length=20)),
                ('Edificio', models.CharField(max_length=10)),
                ('Piso', models.CharField(choices=[('PB', 'BAJA'), ('P1', 'UNO'), ('P2', 'DOS')], default='PB', max_length=2)),
            ],
        ),
    ]