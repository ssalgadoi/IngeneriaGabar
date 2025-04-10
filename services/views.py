from django.shortcuts import render, get_object_or_404
from .models import Services

# Vista para mostrar el detalle de un servicio
def service_detail(request, id):
    service = get_object_or_404(Services, id=id)  # Obtiene el servicio por su ID
    return render(request, 'services/services_detail.html', {'service': service})





