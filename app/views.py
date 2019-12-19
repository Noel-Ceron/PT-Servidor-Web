from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import requests

from django.contrib.auth.models import User, Group
#from rest_framework import viewsets
from .forms import newuserform, validarUser, ControlForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate


def controlAPI(ip, comando, tipo):

    dir = ["tv_interruptor/","vol_interruptor/", "mute_interruptor/"]

    url = "http://" + ip + ":8080/control/"+ dir[tipo]
    payload = { 'comando' : comando}
    headers = { 'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "794476ea-34f7-4558-ae2f-6ae9c8c31936"}

    rest=requests.post(url, json=payload, headers = headers)




def info(request):

    if request.method=='POST':
        if('Actualizar_Info' in request.POST):
            controlf = ControlForm(request.POST)
            if controlf.is_valid():

                estado_pantalla = controlf.cleaned_data['EstadoPf']
                estado_tinker = controlf.cleaned_data['EstadoTf']
                estado_vol = controlf.cleaned_data['Volf']
                estado_mute = controlf.cleaned_data['Mutef']
                ip = controlf.cleaned_data['ipf']


                controlAPI(ip, estado_pantalla, 0)
                controlAPI(ip, estado_vol, 1)
                controlAPI(ip, estado_mute, 2)

                context = { 'controlf':controlf}
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

                if(User.objects.filter(username = nombre).exists()):

                    dato_usuario = User.objects.get(username = nombre)

                    if(check_password(contraseña, dato_usuario.password)):
                        context = { 'controlf' : controlf}
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
