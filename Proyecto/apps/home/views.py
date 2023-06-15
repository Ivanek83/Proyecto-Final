from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from . models import Usuario, Archivo
from . import forms

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

@staff_member_required
def subir_archivo(request):
    usuario = Usuario.objects.get(user=request.user)
    usuario_id = usuario.user.id
    if request.method == 'POST':
        usuario = Usuario.objects.get(id=usuario_id)
        archivo = request.FILES['archivo']
        Archivo.objects.create(usuario_fk=usuario.user, archivo=archivo)
        return redirect('home:index')
    
    usuarios = Usuario.objects.all()
    contexto = {'usuarios': usuarios }
    return render(request, 'home/subir_archivo.html', context=contexto)



def planes(request):
    return render(request, 'home/planes.html')

@login_required
def tu_info(request):
    usuario = request.user.usuario
    nombre = usuario.nombre
    imc = usuario.imc
    peso = usuario.peso
    altura = usuario.altura
    intencion = usuario.get_plan_display()
    id_info = usuario.id
    contexto = {
        'nombre': nombre,
        'peso': peso,
        'imc': imc,
        'altura': altura,
        'intencion': intencion,
        'id_info': id_info,
        }
    return render(request, 'home/tu_info.html', contexto)


def contact(request):
    return render(request, 'home/contact.html')

@login_required
def cargar_datos(request):
    if request.method == 'POST':
        form = forms.UsuarioForm(request.POST)
        #usuario = Usuario.objects.get(user=request.user)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.user = request.user  # Asocia el usuario actualmente autenticado
            usuario.save()
            return redirect('home:index')
    else:
        form = forms.UsuarioForm()
        contexto = {'form': form}
        return render(request, 'home/cargar_datos.html', context=contexto)


@login_required
def editar_datos(request):
    usuario = request.user.usuario  # Obtén el objeto Usuario relacionado al usuario logueado
    if request.method == 'POST':
        form = forms.UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = forms.UsuarioForm(instance=usuario)
        contexto = {'form': form}
        return render(request, 'home/editar_datos.html', context=contexto)





#! Esto es lo propio del Login
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, 'home/index.html', {'mensaje_login': f'Bienvenido {usuario}'})
    else: 
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'home/index.html', {"mensaje_register": f"Usuario {username} creado 😀"})

    else:
        form = UserCreationForm()
    return render(request, 'home/register.html', {"form": form})

