from rest_framework import serializers
from agroaccount.models import Agro

class AgroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agro
        fields = ('id', 'title', 'addedBy', 'nextParty', 'transType', 'category','amount')