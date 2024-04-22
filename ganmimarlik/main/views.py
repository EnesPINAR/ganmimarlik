from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    bannerBg = models.BannerBg.objects.all()
    baslik1 = models.AnaSayfaBaslik1.objects.first()
    content1 = models.AnaSayfaYazi1.objects.first()
    img1 = models.AnaSayfaGorsel1.objects.first()
    baslik2 = models.AnaSayfaBaslik2.objects.first()
    content2 = models.AnaSayfaYazi2.objects.first()
    img2 = models.AnaSayfaGorsel2.objects.first()
    
    context = {
        'bannerBg': bannerBg,
        'baslik1': baslik1,
        'content1': content1,
        'img1': img1,
        'baslik2': baslik2,
        'content2': content2,
        'img2': img2,
    }
    return render(request, 'index.html', context)