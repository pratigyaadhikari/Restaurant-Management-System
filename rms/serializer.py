from rest_framework import serializers
from .models import Category, Table, Food


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['id','name']
        # exclude = ['name']      #yo bahek aru lai serialize garni
        
    def save(self, **kwargs):   #esla update ra create ko lagi kam garxa update ra create garda duplicate hudna dedina
        validated_data= self.validated_data  
        category =  Category.objects.filter(name = validated_data.get('name')).count()
        if category > 0:
            raise serializers.ValidationError({"name":"Category with this name already exists."})
        return super().save(**kwargs)

        # def create(self, validated_data):
        #     category =  Category.objects.filter(name = validated_data.get('name')).count()
        #     if category > 0:
        #         raise serializers.ValidationError({"name":"Category with this name already exists."})
        #     return super().create(validated_data)
    
    
        
class TableModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
        
class FoodModelSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category = serializers.StringRelatedField()
    price_with_vat = serializers.SerializerMethodField()
    price_with_discount = serializers.SerializerMethodField()
    
    class Meta:
        model = Food
        # fields = '__all__'
        fields = ['id','name','description','price','price_with_vat','price_with_discount','category_id','category']    
        
    def get_price_with_vat(self,food:Food):
        return food.price * 0.13 + food.price
    
    def get_price_with_discount(self, food:Food):
        return food.price * 0.30 + food.price
    
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
    
    
