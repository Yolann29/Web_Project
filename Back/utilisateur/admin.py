from django.contrib import admin
from utilisateur.models import cmp, permissions, companies, advertisement, JobApplication

class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(companies,CompaniesAdmin)

class CmpAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'first_name', 'username', 'password', 'email', 'permissions', 'companies')

admin.site.register(cmp, CmpAdmin)

class PermissionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(permissions, PermissionsAdmin)

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'cmp', 'companies')

admin.site.register(advertisement, AdvertisementAdmin)

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'first_name', 'email', 'advert', 'applicant')
    
admin.site.register(JobApplication, JobApplicationAdmin)
