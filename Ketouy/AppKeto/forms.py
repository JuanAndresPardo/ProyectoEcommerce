from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User 
from .models import Producto
from django.contrib.auth import update_session_auth_hash

class FormularioRegistroUsuario(UserCreationForm):
    nombre = forms.CharField(max_length=25, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(
        max_length=20,
        label='Usuario',
        widget=forms.TextInput(attrs={'class':'form-control'}),
        error_messages={
            'unique': 'Este nombre de usuario ya está en uso.',
            'max_length': 'El usuario debe tener como máximo 20 caracteres.',
            'invalid': 'El usuario solo puede contener letras, dígitos y @/./+/-/_.',
        }
    )
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('email', 'nombre', 'apellido', 'username', 'password1', 'password2')


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'peso_gramos', 'categoria', 'precio', 'descripcion', 'fotos']

class FormularioEdicionUsuario(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    first_name = forms.CharField(
        max_length=25,
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False 
    )
    last_name = forms.CharField(
        max_length=20,
        label='Apellido',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False 
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=False 
    )

    password1 = forms.CharField(
        label='Nueva Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )
    password2 = forms.CharField(
        label='Confirmar Nueva Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        update_session_auth_hash(self.request, user)
        return user