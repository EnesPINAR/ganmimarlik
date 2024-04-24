from django.shortcuts import render
from . import models
# Create your views here.
def contact(request):
    iletisimBilgileri = models.IletisimBilgileri.objects.first()
    
    context = {
        'contactInfos': iletisimBilgileri,
    }
    return render(request, 'contact.html', context)