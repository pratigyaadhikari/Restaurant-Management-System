from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Table
from .serializer import CategorySerializer, TableSerializer


# Create your views here.
@api_view()
def category(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)    #serialize: to convert queryset to json format
    return Response(serializer.data)

@api_view()
def table(request):
    table = Table.objects.all()
    serializer = TableSerializer(table, many=True)    #serialize: to convert queryset to json format
    return Response(serializer.data)
