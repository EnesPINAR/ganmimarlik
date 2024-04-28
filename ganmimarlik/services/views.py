from django.shortcuts import render
from . import models
# Create your views here.
def architecture(request):
    services = models.MimariServis.objects.all()
    context = {
        'services': services,
        'isInterior': False,
    }
    return render(request, 'services.html', context)

def interior(request):
    services = models.IcMimarlikServisi.objects.all()
    
    context = {
        'services': services,
        'isInterior': True,
    }
    return render(request, 'services.html', context)