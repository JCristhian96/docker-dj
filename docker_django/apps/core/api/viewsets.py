from rest_framework import viewsets
# Models
from apps.core.models import Person
# Seraializers 
from apps.core.api import serializers


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer
    