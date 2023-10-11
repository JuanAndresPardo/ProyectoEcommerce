from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('registro/', views.RegistroUsuario.as_view(), name='registro'),
    path('login/', views.InicioSesion.as_view(), name='login'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('categoria_bebidas/', views.categoria_bebidas, name='categoria_bebidas'),
    path('categoria_chocolates/', views.categoria_chocolates, name='categoria_chocolates'),
    path('categoria_proteinas/', views.categoria_proteinas, name='categoria_proteinas'),
    path('categoria_snacks/', views.categoria_snacks, name='categoria_snacks'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('editar_producto/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('listado_productos/', views.listado_productos, name='listado_productos'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('detalle_producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('editar-usuario/', views.editar_perfil, name='editar_usuario'),
    path('cambiar-contraseña/', views.cambiar_contraseña, name='cambiar_contraseña'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)