from django.db import models

# Create your models here.
class MimarlikProjesi(models.Model):
    name = models.CharField(max_length=30, editable=True, verbose_name='İsim')
    content = models.TextField(max_length=250, editable=True, verbose_name='İçerik (En fazla 250 karakter)')

    def __str__(self):
        return self.name + ' Projesi'

    class Meta:
        verbose_name_plural = 'Mimarlık Projeleri'
    
class IcMimarlikProjesi(models.Model):
    name = models.CharField(max_length=30, editable=True, verbose_name='İsim')
    content = models.TextField(max_length=250, editable=True, verbose_name='İçerik (En fazla 250 karakter)')

    def __str__(self):
        return self.name + ' Projesi'

    class Meta:
        verbose_name_plural = 'İç Mimarlık Projeleri'

class MimarlikProjesiGorselleri(models.Model):
    mimarlikprojesi = models.ForeignKey(MimarlikProjesi, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='service/%Y/%m/%d', editable=True, verbose_name='Görsel')

    class Meta:
        verbose_name_plural = 'Mimarlık Projeleri Görselleri'

class IcMimarlikProjesiGorselleri(models.Model):
    icmimarlikprojesi = models.ForeignKey(IcMimarlikProjesi, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='service/%Y/%m/%d', editable=True, verbose_name='Görsel')

    class Meta:
        verbose_name_plural = 'İç Mimarlık Projeleri Görselleri'
