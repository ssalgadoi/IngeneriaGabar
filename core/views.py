# core/views.py
from django.shortcuts import render
from services.models import Services




def index(request):
    services = Services.objects.all()  # Obtiene todos los servicios
    return render(request, "core/index.html", { 'services': services })



