from django.db import models

class permissions(models.Model):
    name = models.CharField()

    class Meta:
        verbose_name = 'permission'
        verbose_name_plural = 'permissions'

class cmp(models.Model):
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField()
    email = models.EmailField()
    permissions = models.ForeignKey('permissions', on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'cmp'
        verbose_name_plural = 'cmps'