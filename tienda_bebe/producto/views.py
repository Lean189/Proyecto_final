from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto, Categoria, Color, Talle
from .forms import ProductoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

def inicio(request):
    return render(request, "producto/index.html")

def confirmacion_producto(req):
    return render(req, 'producto/confirmacion_producto.html')


class ProductoListView(ListView):
    model = Producto
    template_name = 'producto/listado_productos.html'
    context_object_name = 'productos'
    paginate_by = 10

    def get_queryset(self):
        queryset = Producto.objects.filter(disponible=True).order_by('-creado')
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = queryset.filter(
                Q(nombre__icontains=search_query) |
                Q(categoria__nombre__icontains=search_query)
            )

        return queryset


class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto/detalle_producto.html'
    context_object_name = 'producto'

    def get_queryset(self):
        return Producto.objects.filter(disponible=True).order_by('-creado')


class ProductoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    permission_required = 'producto.add_producto'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('listado_productos')


class ProductoUpdateview(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('listado_productos')
    permission_required = 'producto.change_producto'


class ProductoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Producto
    template_name = 'producto/confirmar_eliminacion.html'
    success_url = reverse_lazy('listado_productos')
    permission_required = 'producto.delete_producto'


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias/listado.html'
    context_object_name = 'categorias'


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['nombre', 'descripcion']
    template_name = 'categorias/formulario.html'

    def form_valid(self, form):
        if Categoria.objects.filter(nombre=form.instance.nombre).exists():
            form.add_error('nombre', 'Esta categoría ya existe.')
            return self.form_invalid(form)
        return super().form_valid(form)


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ['nombre', 'descripcion']
    template_name = 'categorias/formulario.html'
    success_url = reverse_lazy('listado_categorias')


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'categorias/eliminar.html'
    success_url = reverse_lazy('listado_categorias')


class TalleListView(ListView):
    model = Talle
    template_name = 'talles/listado.html'
    context_object_name = 'talles'


class TalleCreateView(LoginRequiredMixin, CreateView):
    model = Talle
    fields = ['nombre']
    template_name = 'talles/formulario.html'
    success_url = reverse_lazy('listado_talles')


class TalleUpdateView(LoginRequiredMixin, UpdateView):
    model = Talle
    fields = ['nombre']
    template_name = 'talles/formulario.html'
    success_url = reverse_lazy('listado_talles')


class TalleDeleteView(LoginRequiredMixin, DeleteView):
    model = Talle
    template_name = 'talles/eliminar.html'
    success_url = reverse_lazy('listado_talles')


class ColorListView(ListView):
    model = Color
    template_name = 'colores/listado.html'
    context_object_name = 'colores'


class ColorCreateView(LoginRequiredMixin, CreateView):
    model = Color
    fields = ['nombre', 'codigo_color']
    template_name = 'colores/formulario.html'
    success_url = reverse_lazy('listado_colores')


class ColorUpdateView(LoginRequiredMixin, UpdateView):
    model = Color
    fields = ['nombre', 'codigo_color']
    template_name = 'colores/formulario.html'
    success_url = reverse_lazy('listado_colores')


class ColorDeleteView(LoginRequiredMixin, DeleteView):
    model = Color
    template_name = 'colores/eliminar.html'
    success_url = reverse_lazy('listado_colores')
