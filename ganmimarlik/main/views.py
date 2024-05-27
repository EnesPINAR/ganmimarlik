from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    bannerBg = models.BannerBg.objects.all()
    icerik = models.AnaSayfaIcerik.objects.all()
    
    context = {
        'bannerBg': bannerBg,
        'icerik': icerik,
    }
    return render(request, 'index.html', context)