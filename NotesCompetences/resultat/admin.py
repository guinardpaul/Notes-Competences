from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.EnumTrimestre)
admin.site.register(models.EnumResultat)
admin.site.register(models.Evaluation)
admin.site.register(models.Resultat)