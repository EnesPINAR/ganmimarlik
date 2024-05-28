from django.shortcuts import render
from . import models
# Create your views here.
def architecture(request):
    projects = models.MimarlikProjesi.objects.all()
    context = {
        'projects': projects,
        'isInterior': False,
    }
    return render(request, 'projects.html', context)

def interior(request):
    projects = models.IcMimarlikProjesi.objects.all()
    
    context = {
        'projects': projects,
        'isInterior': True,
    }
    return render(request, 'projects.html', context)