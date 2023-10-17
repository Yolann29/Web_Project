from django.contrib import admin
from utilisateur.models import cmp, permissions, companies, advertisement, JobApplication

admin.site.register(cmp)
admin.site.register(permissions)
admin.site.register(companies)
admin.site.register(advertisement)
admin.site.register(JobApplication)
