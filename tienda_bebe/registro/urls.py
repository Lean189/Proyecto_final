from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('editar-perfil/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
]