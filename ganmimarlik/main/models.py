from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class BannerBg(models.Model):
    image = models.ImageField(upload_to='banner/%Y/%m/%d', editable=True, verbose_name='Görsel')
    def save(self, *args, **kwargs):
        if not self.pk and BannerBg.objects.exists():
            raise ValidationError(
                "Sadece 1 adet mevcut banner bulunabilir."
            )
            return None

        return super(BannerBg, self).save(*args, **kwargs)
    def __str__(self): 
        return "Ana sayfa arkaplanı"

class AnaSayfaBaslik1(models.Model):
    content = models.CharField(max_length=20, editable=True, verbose_name='Başlık')
    def save(self, *args, **kwargs):
        if not self.pk and AnaSayfaBaslik1.objects.exists():
            raise ValidationError(
                "Sadece 1 adet ana sayfa başlık 1 bulunabilir."
            )
            return None

        return super(AnaSayfaBaslik1, self).save(*args, **kwargs)
    def __str__(self):
        return 'Ana sayfa ilk başlık (En fazla 20 karakter)'

class AnaSayfaYazi1(models.Model):
    content = models.TextField(max_length=500, editable=True, verbose_name='İçerik')
    def save(self, *args, **kwargs):
        if not self.pk and AnaSayfaYazi1.objects.exists():
            raise ValidationError(
                "Sadece 1 adet ana sayfa yazı 1 bulunabilir."
            )
            return None

        return super(AnaSayfaYazi1, self).save(*args, **kwargs)
    def __str__(self):
        return 'Ana sayfa ilk yazı (En fazla 500 karakter)'
    
class AnaSayfaGorsel1(models.Model):
    img1 = models.ImageField(upload_to='homepage/%Y/%m/%d', editable=True, verbose_name='Görsel')
    def save(self, *args, **kwargs):
        if not self.pk and AnaSayfaGorsel1.objects.exists():
            raise ValidationError(
                "Sadece 1 adet ana sayfa görsel 1 bulunabilir."
            )
            return None

        return super(AnaSayfaGorsel1, self).save(*args, **kwargs)
    def __str__(self):
        return 'Ana sayfa ilk görsel'
    
class AnaSayfaBaslik2(models.Model):
    content = models.CharField(max_length=20, editable=True, verbose_name='Başlık')
    def save(self, *args, **kwargs):
        if not self.pk and AnaSayfaBaslik2.objects.exists():
            raise ValidationError(
                "Sadece 1 adet ana sayfa başlık 2 bulunabilir."
            )
            return None

        return super(AnaSayfaBaslik2, self).save(*args, **kwargs)
    def __str__(self):
        return 'Ana sayfa ikinci başlık (En fazla 20 karakter)'
    
class AnaSayfaYazi2(models.Model):
    content = models.TextField(max_length=500, editable=True, verbose_name='İçerik')
    def save(self, *args, **kwargs):
        if not self.pk and AnaSayfaYazi2.objects.exists():
            raise ValidationError(
                "Sadece 1 adet ana sayfa yazı 2 bulunabilir."
            )
            return None

        return super(AnaSayfaYazi2, self).save(*args, **kwargs)
    def __str__(self):
        return 'Ana sayfa ikinci yazı (En fazla 500 karakter)'
    
class AnaSayfaGorsel2(models.Model):
    img2 = models.ImageField(upload_to='homepage/%Y/%m/%d', editable=True, verbose_name='Görsel')
    def save(self, *args, **kwargs):
        if not self.pk and AnaSayfaGorsel2.objects.exists():
            raise ValidationError(
                "Sadece 1 adet ana sayfa görsel 2 bulunabilir."
            )
            return None

        return super(AnaSayfaGorsel2, self).save(*args, **kwargs)
    def __str__(self):
        return 'Ana sayfa ikinci görsel'