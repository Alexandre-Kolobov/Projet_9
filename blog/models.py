from django.conf import settings
from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=128, verbose_name="Titre")
    description = models.CharField(max_length=2048, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Createur")
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)