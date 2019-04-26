from rest_framework import serializers
from restroapi.models import Restro

class RestroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restro
        fields = ('id', 'name', 'email', 'logo', 'phone', 'rating')