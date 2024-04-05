from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class BannerBg(models.Model):
    image = ResizedImageField(upload_to='banner/%Y/%m/%d', editable=True)