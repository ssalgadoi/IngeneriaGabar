from django.contrib import admin
from .models import Services, ServiceImage

# Admin para el modelo ServiceImage (solo el Inline)
class ServiceImageInline(admin.TabularInline):
    model = ServiceImage  # Relación con ServiceImage
    extra = 1  # Solo un formulario vacío adicional por defecto para agregar una imagen

# Admin para el modelo Services
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')  # Muestra título, fecha de creación y actualización
    search_fields = ('title', 'description')  # Permite buscar por título o descripción
    list_filter = ('created', 'updated')  # Filtros por fechas de creación y actualización

    # Incluir el formulario de las imágenes como Inline en el formulario de servicios
    inlines = [ServiceImageInline]

# Registrar los modelos en el admin
admin.site.register(Services, ServicesAdmin)
