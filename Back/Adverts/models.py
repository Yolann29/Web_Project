from django.db import models
from utilisateur.models import cmp

class Annonce(models.Model):
    superuser = models.CharField()         # ForeignKey(cmp, on_delete=models.CASCADE)
    companies_name = models.CharField(max_length=50)
    description = models.CharField()