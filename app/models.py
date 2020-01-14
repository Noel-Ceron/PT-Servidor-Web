from __future__ import unicode_literals

from django.db import models
# Create your models here.
class UserInfo(models.Model):
    User_name = models.CharField(max_length=25)
    User_password = models.CharField(max_length=10)
    User_email = models.CharField(max_length=50)
    def __str__(self):
        return self.User_name



class Pantalla(models.Model):
    PISO1='P1'
    PISOB='PB'
    PISO2='P2'
    PISOS = [
        (PISOB, 'BAJA'),
        (PISO1, 'UNO'),
        (PISO2, 'DOS'),
    ]
    IdPantalla = models.CharField(max_length=20)
    Edificio = models.CharField(max_length=10)
    Piso = models.CharField(max_length=2, choices=PISOS, default=PISOB, )

    def __str__(self):
        return "%s"%(self.IdPantalla)


class Control(models.Model):
    Estado1='Encender'
    Estado2='Apagar'
    Estado3='Error'

    status = [
        (Estado1, '1'),
        (Estado2, '2'),
        (Estado3, '0'),
    ]

    mudo1 = 'Encendido'
    mudo2 = 'Apagado'

    Mudo = [
        (mudo1, '1'),
        (mudo2, '0'),
    ]

    V25 = '25%'
    V50 = '50%'
    V75 = '75%'

    Volumen = [
        (V25, 'V1'),
        (V50, 'V2'),
        (V75, 'V3'),
    ]

    IdControl = models.CharField(max_length=20)
    EstadoP = models.CharField(max_length=8, choices=status, default=Estado3, )
    EstadoT = models.CharField(max_length=8, choices=status, default=Estado3, )
    Mute = models.CharField(max_length=10, choices=Mudo, default=mudo1, )
    Vol = models.CharField(max_length=4, choices=Volumen, default=V25, )
    IP = models.CharField(max_length=16, default = '192.168.0.0')

    def __str__(self):
        return "%s, estado pantalla: %s, estado TinkerBoard: %s"%(self.IdControl, self.EstadoP, self.EstadoT)


class ControlCompleto(models.Model):

    PISO1='P1'
    PISOB='PB'
    PISO2='P2'
    PISOS = [
        (PISOB, 'BAJA'),
        (PISO1, 'UNO'),
        (PISO2, 'DOS'),
    ]

    Estado1='Encender'
    Estado2='Apagar'
    Estado3='Error'

    status = [
        (Estado1, '1'),
        (Estado2, '2'),
        (Estado3, '0'),
    ]

    mudo1 = 'Encendido'
    mudo2 = 'Apagado'

    Mudo = [
        (mudo1, '1'),
        (mudo2, '0'),
    ]

    V25 = '25%'
    V50 = '50%'
    V75 = '75%'

    Volumen = [
        (V25, 'V1'),
        (V50, 'V2'),
        (V75, 'V3'),
    ]

    IdControl = models.CharField(max_length=20)
    EstadoP = models.CharField(max_length=8, choices=status, default=Estado3, )
    EstadoT = models.CharField(max_length=8, choices=status, default=Estado3, )
    Mute = models.CharField(max_length=10, choices=Mudo, default=mudo1, )
    Vol = models.CharField(max_length=4, choices=Volumen, default=V25, )
    IP = models.CharField(max_length=16, default = '0.0.0.0')

    IdPantalla = models.CharField(max_length=20)
    Edificio = models.CharField(max_length=10)
    Piso = models.CharField(max_length=2, choices=PISOS, default=PISOB, )

    def __str__(self):
        return "%s, estado pantalla: %s, estado TinkerBoard: %s"%(self.IdControl, self.EstadoP, self.EstadoT)
