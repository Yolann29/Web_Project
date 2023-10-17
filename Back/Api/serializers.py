from rest_framework import serializers
from utilisateur.models import advertisement, JobApplication, companies

class AnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = advertisement
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = companies
        fields = '__all__'