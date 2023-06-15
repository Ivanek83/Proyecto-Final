from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Archivo(models.Model):
    usuario_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to= 'archivos_logueados') 
    
    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
    
    def __str__(self):
        return f'{self.usuario_fk.username}'



class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, blank=False, null=True)
    apellido = models.CharField(max_length=30, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    peso = models.PositiveIntegerField(blank=False, null=True)
    altura = models.FloatField(blank=False, null=True)
    ELECCION_GENERO = (('H', 'Hombre'), ('M', 'Mujer'))
    genero = models.CharField(max_length=1, choices=ELECCION_GENERO, blank=False, null=True)
    ELECCION_PLAN = (('B', 'Bajar de Peso'), ('M', 'Mantenerlo'), ('S', 'Subir de peso'))
    plan = models.CharField(max_length=1, choices=ELECCION_PLAN, blank=False, null=True)
    
    @property
    def imc(self):
        if self.peso and self.altura:
            imc = self.peso / (self.altura ** 2)
            return round(imc, 2)
        else:
            return None  
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.capitalize()  # Convertir la primera letra en mayúscula
        self.apellido = self.apellido.capitalize()  # Convertir la primera letra en mayúscula
        super(Usuario, self).save(*args, **kwargs)
    
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
    def __str__(self):
        return f"{self.user.username}"    



