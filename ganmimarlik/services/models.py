from django.db import models

# Create your models here.
class MimarlikServisi(models.Model):
    img = models.ImageField(upload_to='service/%Y/%m/%d', editable=True, verbose_name='Görsel')
    name = models.CharField(max_length=30, editable=True, verbose_name='İsim')
    content = models.TextField(max_length=250, editable=True, verbose_name='İçerik (En fazla 250 karakter)')

    def __str__(self):
        return self.name + ' Servisi'
    
class IcMimarlikServisi(models.Model):
    img = models.ImageField(upload_to='service/%Y/%m/%d', editable=True, verbose_name='Görsel')
    name = models.CharField(max_length=30, editable=True, verbose_name='İsim')
    content = models.TextField(max_length=250, editable=True, verbose_name='İçerik (En fazla 250 karakter)')

    def __str__(self):
        return self.name + ' Servisi'