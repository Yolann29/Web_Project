from django.db import models
from utilisateur.models import cmp, companies

class Annonce(models.Model):
    superuser = models.CharField()
    companies_name = models.CharField(max_length=50)
    description = models.CharField()

class JobApplication(models.Model):
    company = models.ForeignKey(companies, on_delete=models.CASCADE)
    applicant = models.ForeignKey(cmp, on_delete=models.CASCADE)
    surname = models.CharField()
    first_name = models.CharField()
    email = models.EmailField()