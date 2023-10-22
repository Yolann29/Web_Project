from rest_framework import serializers
from utilisateur.models import advertisement, JobApplication, companies, cmp

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

class CmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = cmp
        fields = '__all__'