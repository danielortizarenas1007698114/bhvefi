from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField("Nombre:",max_length=45)
    descripcion = models.TextField(max_length=45)
    empresa = models.CharField(max_length=45)
    fecha = models.DateField(null=True)

    def __str__(self):
        return self.nombre











































































































































from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)

    # Python 3
    def __str__(self): 
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()