from django.db import models

class permissions(models.Model):
    name = models.CharField()

    class Meta:
        verbose_name = 'permission'
        verbose_name_plural = 'permissions'

class companies(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'companies'
        verbose_name_plural = 'companies'

def get_first_company():
    return companies.objects.first()

class cmp(models.Model):
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField()
    email = models.EmailField()
    permissions = models.ForeignKey('permissions', on_delete=models.CASCADE, default=1)
    companies = models.ForeignKey('companies', on_delete=models.CASCADE, default=get_first_company)

    class Meta:
        verbose_name = 'cmp'
        verbose_name_plural = 'cmps'

class advertisement(models.Model):
    title = models.CharField()
    description = models.CharField()
    companies = models.ForeignKey('companies', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'advertisement'
        verbose_name_plural = 'advertisements'