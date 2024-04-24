from django.db import models

# Create your models here.
class Servis(models.Model):
    img = models.ImageField(upload_to='service/%Y/%m/%d', editable=True)
    name = models.CharField(max_length=30, editable=True)
    content = models.CharField(max_length=200, editable=True)

    def __str__(self):
        return self.name + 'Servisi'