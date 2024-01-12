from rest_framework import serializers
from .models import Query

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ['id', 'query', 'k_value']