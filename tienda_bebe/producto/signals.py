from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from .models import Producto

@receiver(post_migrate)
def asignar_permisos_producto(sender, **kwargs):
    
    content_type = ContentType.objects.get_for_model(Producto)
    
    # Crear permisos si no existen
    Permission.objects.get_or_create(
        codename='add_producto',
        name='Can add producto',
        content_type=content_type
    )
    Permission.objects.get_or_create(
        codename='change_producto',
        name='Can change producto',
        content_type=content_type
    )
    Permission.objects.get_or_create(
        codename='delete_producto',
        name='Can delete producto',
        content_type=content_type
    )
    
    
    group, created = Group.objects.get_or_create(name='Scrum')
    
    
    scrum_permissions = Permission.objects.filter(content_type=content_type)
    group.permissions.set(scrum_permissions)
    group.save()



