from django.shortcuts import render
from . import models
# Create your views here.
def services(request):
    services = models.Servis.objects.all()
    
    context = {
        'services': services,
    }
    return render(request, 'services.html', context)