from django.db import models

# Create your models here.
class Hakkinda(models.Model):
    content = models.TextField(max_length=4000, verbose_name='İçerik (En fazla 4000 karakter)')
    def __str__(self):
        return 'Hakkında Yazısı'