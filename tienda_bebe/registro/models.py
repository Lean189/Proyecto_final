from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    class Meta:
        permissions = [
            ("puede_hacer_scrum", "Puede hacer Scrum"),
        ]
    
    def __str__(self):
        return self.username