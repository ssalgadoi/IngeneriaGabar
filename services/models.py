from django.db import models
from django.contrib.auth.models import User
# Importar BaseModel desde el mismo archivo si está en el mismo directorio
from core.models import BaseModel  

# Modelo Services hereda de BaseModel
class Services(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    content = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(upload_to='services/images/', verbose_name="Imagen")
    # Los campos created y updated serán heredados de BaseModel

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.title} - {self.description}"




class ServiceImage(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='imagenes')
    image = models.ImageField(verbose_name="Imagen", upload_to="services/images", null=True, blank=True)

    class Meta:
        verbose_name = "Imagen de servicio"
        verbose_name_plural = "Imágenes de servicio"
