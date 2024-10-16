from rest_framework import serializers
from skinserver.models import User, Hospital, History

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('id', 'name', 'image', 'specialties')
        
class HospitalDeailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
        
class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'