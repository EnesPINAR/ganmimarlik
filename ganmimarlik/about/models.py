from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Hakkinda(models.Model):
    content = models.TextField(max_length=4000, verbose_name='İçerik (En fazla 4000 karakter)')

    def save(self, *args, **kwargs):
        if not self.pk and Hakkinda.objects.exists():
            raise ValidationError(
                "Sadece 1 adet mevcut hakkında yazısı bulunabilir."
            )
            return None

        return super(Hakkinda, self).save(*args, **kwargs)
    def __str__(self):
        return 'Hakkında Yazısı'

    class Meta:
        verbose_name_plural = 'Hakkında Yazısı'