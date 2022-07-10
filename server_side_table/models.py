from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class ApiDatatable(models.Model):

    organization_name = models.CharField(_("Organizaion name"), max_length=50)
    api_name = models.CharField(_("Api name"), max_length=120)
    date = models.DateField(_("Date"), auto_now_add=True)
    usages = models.IntegerField(_("Usages"))

    def __str__(self) -> str:
        return self.organization_name