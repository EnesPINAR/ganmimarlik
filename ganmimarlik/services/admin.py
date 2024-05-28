from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.MimarlikProjesi)
admin.site.register(models.MimarlikProjesiGorselleri)
admin.site.register(models.IcMimarlikProjesi)
admin.site.register(models.IcMimarlikProjesiGorselleri)