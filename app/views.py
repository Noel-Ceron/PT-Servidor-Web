from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import time
import requests
from wakeonlan import send_magic_packet

from app.models import Control, Pantalla, ControlCompleto

from django.contrib.auth.models import User, Group
#from rest_framework import viewsets
from .forms import newuserform, validarUser, ControlForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate

info_control = ControlCompleto.objects.all()

def controlAPI(ip, comando, tipo, tinkerNumero):

    try:
        if (comando=='1' and tipo==3):
            macs = ['88:d7:f6:c3:3b:d7', '0c:9d:92:0c:98:b8']
            #print('aqui')
            send_magic_packet('ff.ff.ff.ff.ff.ff', macs[tinkerNumero], 'FFFFFFFFFFFF')

        #print(comando)
        dir = ["tv_interruptor/","vol_interruptor/", "mute_interruptor/", "tinker_interruptor/"]

        url = "http://" + ip + ":8080/control/"+ dir[tipo]
        payload = { 'comando' : comando}
        headers = { 'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "794476ea-34f7-4558-ae2f-6ae9c8c31936"}

        requests.post(url, json=payload, headers = headers)

        if(tipo==0):
            ControlCompleto.objects.filter(IdControl=info_control[tinkerNumero].IdControl).update(EstadoP='Encender')
            pass
        elif(tipo==1):
            pass
        elif(tipo==2):
            pass
        elif(tipo==3):
            ControlCompleto.objects.filter(IdControl=info_control[tinkerNumero].IdControl).update(EstadoT='Encender')
            ControlCompleto.objects.filter(IdControl=info_control[tinkerNumero].IdControl).update(EstadoP='Encender')
            pass
        else:
            print("Ocurrio un error al enviar el comando")

    except requests.exceptions.RequestException as e:

        if(tipo==0):
            ControlCompleto.objects.filter(IdControl=info_control[tinkerNumero].IdControl).update(EstadoP='Error')
            pass
        elif(tipo==1):
            pass
        elif(tipo==2):
            pass
        elif(tipo==3):
            ControlCompleto.objects.filter(IdControl=info_control[tinkerNumero].IdControl).update(EstadoT='Error')
            ControlCompleto.objects.filter(IdControl=info_control[tinkerNumero].IdControl).update(EstadoP='Error')
            pass
        else:
            print("Ocurrio un error al enviar el comando")




def info(request):
    info_control = ControlCompleto.objects.all()

    if request.method=='POST':
        if('Actualizar_Info' in request.POST):
            controlf = ControlForm(request.POST)
            if controlf.is_valid():

                controlf2 = ControlForm()
                estado_pantalla = controlf.cleaned_data['EstadoPf']
                estado_tinker = controlf.cleaned_data['EstadoTf']
                estado_vol = controlf.cleaned_data['Volf']
                estado_mute = controlf.cleaned_data['Mutef']

                #print("estado")
                #print(estado_tinker)
                ip = info_control[0].IP

                if(estado_tinker=='1'):
                    #print('aqui2')
                    controlAPI(ip, estado_tinker, 3, 0)
                    time.sleep(1)
                    controlAPI(ip, estado_mute, 2, 0)
                    time.sleep(1)
                    controlAPI(ip, estado_vol, 1, 0)
                    controlAPI(ip, estado_pantalla, 0, 0)


                else:
                    controlAPI(ip, estado_pantalla, 0, 0)
                    time.sleep(3)
                    controlAPI(ip, estado_mute, 2, 0)
                    time.sleep(1)
                    controlAPI(ip, estado_vol, 1, 0)
                    time.sleep(1)
                    controlAPI(ip, estado_tinker, 3, 0)

                context = { 'controlf':controlf, 'controlf2':controlf2, 'info_control' : info_control}
                template = loader.get_template('app/index3.html')
                return HttpResponse(template.render(context, request))

            else:
                controlf = ControlForm()
                context = { 'controlf':controlf}
                template = loader.get_template('app/index3.html')
                return HttpResponse(template.render(context, request))


        elif('Actualizar_Info2' in request.POST):
            controlf2 = ControlForm(request.POST)
            if controlf2.is_valid():
                controlf = ControlForm()
                estado_pantalla = controlf2.cleaned_data['EstadoPf']
                estado_tinker = controlf2.cleaned_data['EstadoTf']
                estado_vol = controlf2.cleaned_data['Volf']
                estado_mute = controlf2.cleaned_data['Mutef']

                ip = info_control[1].IP

                if(estado_tinker=='1'):
                    #print('aqui2')
                    controlAPI(ip, estado_tinker, 3, 1)
                    time.sleep(1)
                    controlAPI(ip, estado_mute, 2, 1)
                    time.sleep(1)
                    controlAPI(ip, estado_vol, 1, 1)
                    controlAPI(ip, estado_pantalla, 0, 1)


                else:
                    controlAPI(ip, estado_pantalla, 0, 1)
                    time.sleep(3)
                    controlAPI(ip, estado_mute, 2, 1)
                    time.sleep(1)
                    controlAPI(ip, estado_vol, 1, 1)
                    time.sleep(1)
                    controlAPI(ip, estado_tinker, 3, 1)

                context = { 'controlf':controlf, 'controlf2':controlf2, 'info_control' : info_control}
                template = loader.get_template('app/index3.html')
                return HttpResponse(template.render(context, request))

            else:
                controlf = ControlForm()
                context = { 'controlf':controlf}
                template = loader.get_template('app/index3.html')
                return HttpResponse(template.render(context, request))


    else:

        controlf = ControlForm()
        context = { 'controlf':controlf}
        template = loader.get_template('app/index3.html')
        return HttpResponse(template.render(context, request))


def index(request):

    s = User.objects.all()
    if(request.method == 'POST'):
        if('registrar' in request.POST):
            t=newuserform(request.POST)

            if t.is_valid():
                nombre = t.cleaned_data['nombre']
                correo = t.cleaned_data['correo']
                contraseña = make_password(t.cleaned_data['contraseña'], salt = None, hasher='default')

                User.objects.create(username=nombre, email=correo, password = contraseña)
                r = validarUser()
                context = {'s':s, 't':t, 'r':r}
                template = loader.get_template('app/login.html')
                return HttpResponse(template.render(context, request))

        elif('verificar' in request.POST):

            r = validarUser(request.POST)

            if r.is_valid():
                nombre = r.cleaned_data['nombre']
                contraseña = r.cleaned_data['contraseña']

                controlf = ControlForm()
                controlf2 = ControlForm()

                if(User.objects.filter(username = nombre).exists()):

                    dato_usuario = User.objects.get(username = nombre)

                    if(check_password(contraseña, dato_usuario.password)):

                        info_control = ControlCompleto.objects.all()

                        context = { 'controlf':controlf, 'controlf2':controlf2,
                         'info_control' : info_control , 'nombreUsuario' : nombre }


                        template = loader.get_template('app/index3.html')

                        return HttpResponse(template.render(context, request))

                    else:
                        t=newuserform()
                        r = validarUser()

                        context = {'s':s, 't':t, 'r':r}
                        template = loader.get_template('app/login.html')
                        return HttpResponse(template.render(context, request))

                else:
                    t=newuserform()
                    r = validarUser()

                    context = {'s':s, 't':t, 'r':r}
                    template = loader.get_template('app/login.html')
                    return HttpResponse(template.render(context, request))

            else:
                t=newuserform()
                r = validarUser()

                context = {'s':s, 't':t, 'r':r}
                template = loader.get_template('app/login.html')
                return HttpResponse(template.render(context, request))


    else:
        t=newuserform()
        r = validarUser()

        context = {'s':s, 't':t, 'r':r}
        template = loader.get_template('app/login.html')
        return HttpResponse(template.render(context, request))



def gentella_html(request):
    context = {
    }
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)

    return HttpResponse(template.render(context, request))
