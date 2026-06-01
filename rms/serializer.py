from rest_framework import serializers
from .models import Category, Table


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['id','name']
        # exclude = ['name']      #yo bahek aru lai serialize garni
        
class TableModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

# class CategorySerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only = True)
    # name = serializers.CharField()
    
    # def create(self, validated_data):
    #     category = Category.objects.create(name = validated_data.get('name'))
    #     return category
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance
        
        
class TableSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    number = serializers.CharField()
    capacity = serializers.CharField()
    is_available = serializers.BooleanField()
    
    def create(self, validated_data):
        table = Table.objects.create(**validated_data)
        return table
    
    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.is_available = validated_data.get('is_available', instance.is_available)
        instance.save()
        return instance
    
    
