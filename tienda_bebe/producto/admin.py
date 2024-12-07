from django.contrib import admin
from .models import Producto, Talle, Color , ProductoAdmin

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Talle)
admin.site.register(Color)
