from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm, FormularioRegistroUsuario, FormularioEdicionUsuario, PasswordChangeForm
from django.contrib.auth import login
from .models import Producto, Categoria
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from random import sample
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def inicio(request):
    todos_los_productos = Producto.objects.all()

    productos_al_azar = sample(list(todos_los_productos), 8)

    return render(request, 'inicio.html', {'productos_al_azar': productos_al_azar})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()

    categorias = Categoria.objects.all()

    return render(request, 'crear_producto.html', {'form': form, 'categorias': categorias})
def vista_ejemplo(request):
    producto = Producto.objects.get(pk=1)
    return render(request, 'productos.html', {'producto': producto})

def is_staff_user(user):
    return user.is_staff

@user_passes_test(is_staff_user)
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')

    return render(request, 'eliminar_producto.html', {'producto': producto})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

class RegistroUsuario(FormView):
    template_name = 'RegistrarUsuario.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('registro')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroUsuario, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.info(self.request, 'Ya estás registrado y autenticado.')
            return redirect(reverse_lazy('inicio'))
        return super(RegistroUsuario, self).get(*args, **kwargs)
    

class InicioSesion(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('inicio')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = FormularioEdicionUsuario(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')
    else:
        form = FormularioEdicionUsuario(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})

def cambiar_contraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Actualiza la sesión del usuario.
            messages.success(request, 'Tu contraseña ha sido modificada con éxito.')
            return redirect('perfil')  # Redirige a la página de perfil o donde desees.
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'cambiar_contraseña.html', {'form': form})

def nosotros(request):
    return render(request, 'nosotros.html')

def categoria_bebidas(request):
    productos = Producto.objects.filter(categoria__nombre='Bebidas')
    return render(request, 'categoria_bebidas.html', {'productos': productos})

def categoria_chocolates(request):
    productos = Producto.objects.filter(categoria__nombre='Chocolates')
    return render(request, 'categoria_chocolates.html', {'productos': productos})

def categoria_proteinas(request):
    productos = Producto.objects.filter(categoria__nombre='Proteinas')
    return render(request, 'categoria_proteinas.html', {'productos': productos})

def categoria_snacks(request):
    productos = Producto.objects.filter(categoria__nombre='Snacks')
    return render(request, 'categoria_snacks.html', {'productos': productos})

def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'Listado_productos.html', {'productos': productos})

