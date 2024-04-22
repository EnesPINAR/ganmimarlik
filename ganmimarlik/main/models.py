from django.db import models

# Create your models here.
class BannerBg(models.Model):
    image = models.ImageField(upload_to='banner/%Y/%m/%d', editable=True)
    def __str__(self): 
        return "Ana sayfa arkaplanı"

class AnaSayfaBaslik1(models.Model):
    content = models.CharField(max_length=20, editable=True)
    def __str__(self):
        return 'Ana sayfa ilk başlık'

class AnaSayfaYazi1(models.Model):
    content = models.CharField(max_length=500, editable=True)
    def __str__(self):
        return 'Ana sayfa ilk yazı'
    
class AnaSayfaGorsel1(models.Model):
    img1 = models.ImageField(upload_to='homepage/%Y/%m/%d', editable=True)
    def __str__(self):
        return 'Ana sayfa ilk görsel'
    
class AnaSayfaBaslik2(models.Model):
    content = models.CharField(max_length=20, editable=True)
    def __str__(self):
        return 'Ana sayfa ikinci başlık'
    
class AnaSayfaYazi2(models.Model):
    content = models.CharField(max_length=500, editable=True)
    def __str__(self):
        return 'Ana sayfa ikinci yazı'
    
class AnaSayfaGorsel2(models.Model):
    img2 = models.ImageField(upload_to='homepage/%Y/%m/%d', editable=True)
    def __str__(self):
        return 'Ana sayfa ikinci görsel'