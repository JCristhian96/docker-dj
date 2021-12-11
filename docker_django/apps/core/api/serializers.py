from rest_framework import serializers
# Models Apps Core
from apps.core.models import Person


class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = "__all__"
    
