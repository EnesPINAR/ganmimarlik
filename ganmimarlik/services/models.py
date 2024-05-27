from django.db import models

# Create your models here.
class MimarlikServisi(models.Model):
    name = models.CharField(max_length=30, editable=True, verbose_name='İsim')
    content = models.TextField(max_length=250, editable=True, verbose_name='İçerik (En fazla 250 karakter)')

    def __str__(self):
        return self.name + ' Hizmeti'

    class Meta:
        verbose_name_plural = 'Mimarlık Hizmetleri'
    
class IcMimarlikServisi(models.Model):
    name = models.CharField(max_length=30, editable=True, verbose_name='İsim')
    content = models.TextField(max_length=250, editable=True, verbose_name='İçerik (En fazla 250 karakter)')

    def __str__(self):
        return self.name + ' Hizmeti'

    class Meta:
        verbose_name_plural = 'İç Mimarlık Hizmetleri'

class MimarlikServisiGorselleri(models.Model):
    mimarlikservisi = models.ForeignKey(MimarlikServisi, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='service/%Y/%m/%d', editable=True, verbose_name='Görsel')

    class Meta:
        verbose_name_plural = 'Mimarlık Hizmetleri Görselleri'

class IcMimarlikServisiGorselleri(models.Model):
    mimarlikservisi = models.ForeignKey(IcMimarlikServisi, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='service/%Y/%m/%d', editable=True, verbose_name='Görsel')

    class Meta:
        verbose_name_plural = 'İç Mimarlık Hizmetleri Görselleri'
