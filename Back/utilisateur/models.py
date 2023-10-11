from django.db import models

class cmp(models.Model):
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField()
    email = models.EmailField()





