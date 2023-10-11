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
    id_permissions = models.ForeignKey('permissions', on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'cmp'
        verbose_name_plural = 'cmps'

class jobapplication(models.Model):
    id_cmp = models.ForeignKey('cmp', on_delete=models.CASCADE)
    id_advertisement = models.ForeignKey('advertisement', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'jobapplication'
        verbose_name_plural = 'jobapplications'

class companie(models.Model):
    name = models.CharField()

    class Meta:
        verbose_name = 'companie'
        verbose_name_plural = 'companies'

class advertisement(models.Model):
    name = models.CharField()
    id_companies = models.ForeignKey('companie', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'advertisement'
        verbose_name_plural = 'advertisements'