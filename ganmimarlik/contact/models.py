from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class IletisimBilgileri(models.Model):
    phoneRegex = RegexValidator(regex=r'^\+\d{8,15}$', message="Telefon numarası şu formatta olmalıdır: '+999999999' ve en fazla 15 karakter girilebilir.")
    phoneNumber = models.CharField(validators=[phoneRegex], max_length=17, blank=True, verbose_name='Telefon Numarası (Ülke kodu da girilmeli)')
    eMail = models.CharField(validators=[validate_email], max_length=100, blank=True, verbose_name='E-Posta')
    instagram = models.CharField(max_length=100, blank=True, verbose_name='Instagram linki')
    x = models.CharField(max_length=100, blank=True, verbose_name='X linki')
    facebook = models.CharField(max_length=100, blank=True, verbose_name='Facebook linki')
    maps = models.CharField(max_length=1000, blank=True, verbose_name='Google haritalar linki')
    def __str__(self):
        return 'İletişim Bilgileri'

    def save(self, *args, **kwargs):
        if not self.pk and IletisimBilgileri.objects.exists():
            raise ValidationError(
                "Sadece 1 adet iletişim bilgileri bulunabilir. Var olan iletişim bilgilerini güncellemek için eski iletişim bilgilerinin üstüne tıklayın."
            )
            return None

        return super(IletisimBilgileri, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'İletişim Bilgileri'