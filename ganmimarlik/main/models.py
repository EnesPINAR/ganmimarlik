from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Model


# Create your models here.
class BannerBg(models.Model):
    image = models.ImageField(upload_to='banner/%Y/%m/%d', editable=True, verbose_name='Görsel', unique=True)
    def save(self, *args, **kwargs):
        if not self.pk and BannerBg.objects.exists():
            raise ValidationError(
                "Sadece 1 adet mevcut ana sayfa arka planı bulunabilir."
            )
            return None

        return super(BannerBg, self).save(*args, **kwargs)
    def __str__(self): 
        return "Ana sayfa arkaplanı"

    class Meta:
        verbose_name_plural = 'Ana Sayfa Arka Planı'

class AnaSayfaIcerik(models.Model):
    image = models.ImageField(upload_to='banner/%Y/%m/%d', editable=True, verbose_name='Görsel')
    title = models.CharField(max_length=20, editable=True, verbose_name='Başlık')
    content = models.TextField(max_length=500, editable=True, verbose_name='İçerik')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Ana Sayfa İçerikleri'
