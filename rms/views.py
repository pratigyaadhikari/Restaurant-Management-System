from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Table, OrderItem
from .serializer import CategorySerializer, TableSerializer


# Create your views here.
@api_view(['GET','POST'])
def category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)    #serialize: to convert queryset to json format
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data = request.data)    #deserialize: json format convert to model instance
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET','POST','DELETE'])
def category_detail(request, id):
    category = Category.objects.get(id = id)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(category, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        items = OrderItem.objects.filter(food__category = category).count()
        if items > 0:
            return Response({"detail":"category cannoy be deleted. Protected in OrderItem"})
        category.delete()
        return Response({"detail": "Category deleted successfully"})
    
    
@api_view(['GET','POST'])
def table(request):
    if request.method == 'GET':
        table = Table.objects.all()
        serializer = TableSerializer(table, many=True)    #serialize: to convert queryset to json format
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TableSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET','POST'])
def table_detail(request, id):
    table = Table.objects.get(id = id)
    if request.method == 'GET':
        serializer = TableSerializer(table)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TableSerializer(table, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
        

