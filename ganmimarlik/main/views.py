from django.shortcuts import render
from .models import BannerBg

# Create your views here.
def index(request):
    bannerBg = BannerBg.objects.all()
    return render(request, 'index.html', {'bannerBg': bannerBg})