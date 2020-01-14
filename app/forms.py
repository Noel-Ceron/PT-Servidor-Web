from django import forms

class newuserform(forms.Form):
    nombre=forms.CharField(label='Inserta tu nombre',max_length=30)
    correo=forms.EmailField(label='Inserta aqui tu correo')
    contraseña=forms.CharField(label='Contraseña', widget=forms.PasswordInput())

class validarUser(forms.Form):
    nombre=forms.CharField(label='Inserta tu nombre',max_length=30)
    contraseña=forms.CharField(label='Contraseña', widget=forms.PasswordInput())


class ControlForm(forms.Form):
    Estado1 = 1
    Estado2 = 2
    Estado3 = 0

    status = [
        (Estado1, 'Encender'),
        (Estado2, 'Apagar'),
        (Estado3, 'Error'),
    ]

    mudo1 = 1
    mudo2 = 0

    Mudo = [
        (mudo1, 'Encendido'),
        (mudo2, 'Apagado'),
    ]

    V25 = '25%'
    V50 = '50%'
    V75 = '80%'

    Volumen = [
        (V25, '25%'),
        (V50, '50%'),
        (V75, '80%'),
    ]

    EstadoPf = forms.ChoiceField(choices=status, )
    EstadoTf = forms.ChoiceField(choices=status, )
    Mutef = forms.ChoiceField(choices=Mudo, )
    Volf = forms.ChoiceField(choices=Volumen, )

    def __str__(self):
        return "estado pantalla: %s, estado TinkerBoard: %s"%( self.EstadoPf, self.EstadoTf)
