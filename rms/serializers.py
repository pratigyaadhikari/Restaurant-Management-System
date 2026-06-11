from rest_framework import serializers
from .models import Category, Table, Food, Order, OrderItem, Reservation


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
    
  
class OrderItemModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = ['food']
        
    
class OrderModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    item = OrderItemModelSerializer(many=True)
    status = serializers.CharField(read_only = True)
    payment_status = serializers.CharField(read_only = True)
    total_price = serializers.IntegerField(read_only = True)
    
    class Meta:
        model = Order    
        fields = ['id','user','total_price','status','payment_status','item']
    
    def create(self, validated_data):
        items = validated_data.pop('item')
        total_price = 0
        for item in items:
            food_item = item.get('food')        #food_item = 3840
            total_price += food_item.price
        order = Order.objects.create(total_price=total_price, **validated_data)
        for item in items:
            OrderItem.objects.create(order = order, food = item.get('food'))
        return order
        
# validated_data = {}
# items = {"item": [{"food":2840}]}  {
 

class ReservationModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    table_id = serializers.PrimaryKeyRelatedField(queryset=Table.objects.all(),source='table')
    table = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Reservation
        fields = ['id','user','table_id','table','time','total_users']
    
    def validate(self, data):
        table = data['table']
        time = data['time']

        if Reservation.objects.filter(table=table, time=time).exists():
            raise serializers.ValidationError(
                {"table": "This table is already reserved for that time."}
            )

        return data
    


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
        
        
# class TableSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     number = serializers.CharField()
#     capacity = serializers.CharField()
#     is_available = serializers.BooleanField()
    
#     def create(self, validated_data):
#         table = Table.objects.create(**validated_data)
#         return table
    
#     def update(self, instance, validated_data):
#         instance.number = validated_data.get('number', instance.number)
#         instance.capacity = validated_data.get('capacity', instance.capacity)
#         instance.is_available = validated_data.get('is_available', instance.is_available)
#         instance.save()
#         return instance
    
    
