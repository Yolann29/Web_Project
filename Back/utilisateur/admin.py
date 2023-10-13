from django.contrib import admin
from utilisateur.models import cmp, permissions, jobapplication, companie, advertisement

admin.site.register(cmp)
admin.site.register(permissions)
admin.site.register(jobapplication)
admin.site.register(companie)
admin.site.register(advertisement)
