from rest_framework import serializers
from .models import  Personnal

class PersonnalSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Personnal
        fields = "__all__" 