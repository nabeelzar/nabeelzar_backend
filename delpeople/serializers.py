from rest_framework import serializers
from delpeople.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person 
        fields = ['id', 'first_name', 'last_name', 'datetime']