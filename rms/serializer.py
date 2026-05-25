from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    
class TableSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    number = serializers.CharField()
    capacity = serializers.CharField()
    is_available = serializers.BooleanField()
    
