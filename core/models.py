from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        abstract = True
        
    def __str__(self):
        return str(self.author)  # Devolver una representación en cadena del autor
