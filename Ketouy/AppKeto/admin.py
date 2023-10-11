from django.contrib import admin
from .models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'peso_gramos', 'categoria', 'precio')
    list_filter = ('categoria', 'marca', 'nombre')
    search_fields = ('nombre', 'marca', 'descripcion')

admin.site.register(Producto, ProductoAdmin)