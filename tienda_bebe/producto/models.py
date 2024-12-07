from django.db import models
from django.contrib.auth.models import User , Group , Permission
from django.urls import reverse
from django.contrib import admin


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('listado_categorias')
    


class Talle(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Color(models.Model):
    nombre = models.CharField(max_length=50)
    codigo_color = models.CharField(max_length=7) 

    def __str__(self):
        return self.nombre

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio', 'stock', 'disponible', 'categoria']
    search_fields = ['nombre', 'descripcion']
    list_filter = ['categoria', 'disponible']


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='media/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
    talle = models.ManyToManyField(Talle)
    color = models.ManyToManyField(Color)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def reducir_stock(self, cantidad):
        """Reduce la cantidad de stock si es suficiente, de lo contrario lanza un error."""
        if self.stock >= cantidad:
            self.stock -= cantidad
            self.save()
        else:
            raise ValueError("Stock insuficiente")

    def precio_final(self):
        """Calcula el precio final del producto considerando una oferta activa."""
        from django.utils.timezone import now
        ofertas = self.oferta_set.filter(fecha_inicio__lte=now(), fecha_fin__gte=now())
        if ofertas.exists():
            descuento = ofertas.first().descuento_porcentaje
            return self.precio * (1 - descuento / 100)
        return self.precio



class Oferta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="ofertas")
    descuento_porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return f"{self.producto.nombre} - {self.descuento_porcentaje}%"

#aca todo lo del scrum


permiso_crear_producto = Permission.objects.get(codename='add_producto')
permiso_editar_producto = Permission.objects.get(codename='change_producto')
permiso_eliminar_producto = Permission.objects.get(codename='delete_producto')


