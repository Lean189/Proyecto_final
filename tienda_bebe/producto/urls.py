from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    inicio,
    ProductoListView, ProductoCreateView, ProductoUpdateview, ProductoDeleteView,
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView,
    TalleListView, TalleCreateView, TalleUpdateView, TalleDeleteView,
    ColorListView, ColorCreateView, ColorUpdateView, ColorDeleteView,
    confirmacion_producto,
)

urlpatterns = [
    path('index/', inicio, name='index'),

    path('productos/', ProductoListView.as_view(), name='listado_productos'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='crear_producto'),
    path('productos/<int:pk>/editar/', ProductoUpdateview.as_view(), name='editar_producto'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='eliminar_producto'),
    path('productos/confirmacion/', confirmacion_producto, name='confirmacion_producto'),

    path('categorias/', CategoriaListView.as_view(), name='listado_categorias'),
    path('categorias/nueva/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('categorias/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='eliminar_categoria'),

    path('talles/', TalleListView.as_view(), name='listado_talles'),
    path('talles/nuevo/', TalleCreateView.as_view(), name='crear_talle'),
    path('talles/<int:pk>/editar/', TalleUpdateView.as_view(), name='editar_talle'),
    path('talles/<int:pk>/eliminar/', TalleDeleteView.as_view(), name='eliminar_talle'),

    path('colores/', ColorListView.as_view(), name='listado_colores'),
    path('colores/nuevo/', ColorCreateView.as_view(), name='crear_color'),
    path('colores/<int:pk>/editar/', ColorUpdateView.as_view(), name='editar_color'),
    path('colores/<int:pk>/eliminar/', ColorDeleteView.as_view(), name='eliminar_color'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

