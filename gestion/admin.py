from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Classe)
admin.site.register(models.Eleve)
admin.site.register(models.Domaine)
admin.site.register(models.Competence)
