from django.db import models

# Create your models here.
class BannerBg(models.Model):
    image = models.ImageField(upload_to='banner/%Y/%m/%d', editable=True)