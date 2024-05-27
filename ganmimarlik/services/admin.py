from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.MimarlikServisi)
admin.site.register(models.MimarlikServisiGorselleri)
admin.site.register(models.IcMimarlikServisi)
admin.site.register(models.IcMimarlikServisiGorselleri)