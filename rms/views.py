from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Table, OrderItem, Food
# from .serializer import CategorySerializer, TableSerializer
from .serializers import CategoryModelSerializer, TableModelSerializer, FoodModelSerializer
from .pagination import CategoryPagination, TablePagination, FoodPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filter import FoodFilter

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

# from rest_framework.permissions import IsAuthenticatedOrReadOnly #(IsAuthenticated)
from .permissions import IsAuth
# Create your views here.
from rest_framework import viewsets
# Model viewset:

class CategoryModelViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    # pagination_class = CategoryPagination
    
    permission_classes = [IsAuth]
    
    @extend_schema(
        parameters=[OpenApiParameter(name='name', description='Name of the category', type=OpenApiTypes.STR)],
        description='This handles category list',
    )
    def list(self,request,*args,**kwargs):
        return super().list(request, *args, **kwargs)
    
    def destroy(self, request, pk):
        category =  Category.objects.get(pk = pk)
        items = OrderItem.objects.filter(food__category = category).count()
        if items > 0:
            return Response({"details":"category cannot be deleted. Protected in OrderItem"})
        category.delete()
        return Response({"details":"Category deleted successfully"})
    
     
class TableModelViewset(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableModelSerializer
    pagination_class = TablePagination
    
class FoodModelviewset(viewsets.ModelViewSet):  
    queryset = Food.objects.select_related('category').all()
    serializer_class = FoodModelSerializer
    pagination_class = FoodPagination
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['name']    #if tuple ('name',) ma name rakhni ho vane euta field matra rakhda field paxi (,) yo rakhni dherai vayo vane rakhna pardaina ('name','price')
    # filterset_fields = ['category']   #if  class create nagare fields ma directly add garna this one
    filterset_class = FoodFilter #manually class create garexa vane yo use garni
    
    
# Viewset:

# class CategoryViewset(viewsets.ViewSet):
#     def list(self, request):         
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many = True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = CategorySerializer(data = request.data)    #deserialize: json format convert to model instance
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
        
    
# class CategoryDetailViewset(viewsets.ViewSet):
#     def retrieve(self, request, pk):
#         category = Category.objects.get(pk = pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data) 
#     def update(self, request, pk):
#         category = Category.objects.get(pk = pk)
#         serializer = CategorySerializer(category, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def partial_update(self,request,pk):
#         category = Category.objects.get(pk = pk)
#         serializer = CategorySerializer(category, data = request.data, partial = True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)        
#     def destroy(self, request, pk):
#         category =  Category.objects.get(pk = pk)
#         items = OrderItem.objects.filter(food__category = category).count()
#         if items > 0:
#             return Response({"details":"category cannot be deleted. Protected in OrderItem"})
#         category.delete()
#         return Response({"details":"Category deleted successfully"})
    
    


# Mixins:
# from rest_framework import mixins, generics

# class CategoryGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
#     def get(self,request):
#         return self.list(request)       #if useing mixin yo line matra lekhda vo insted of mathi ko 3 ota line code
        
#         # category = Category.objects.all()
#         # serializer = CategorySerializer(category, many = True)
#         # return Response(serializer.data)
        
#     def post(self, request):
#         return self.create(request)
        
# class CategoryDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     # lookup_field = 'id'
#     # (if lookup field use gardina vaneni , we can use pk)
#     def get(self,request,pk):       #id = pk rakhni
#         return self.retrieve(request, pk)
    
#     def post(self,request,pk):
#         return self.update(request, pk)
    
#     def delete(self,request,pk):
#         category =  Category.objects.get(id = pk)
#         items = OrderItem.objects.filter(food__category = category).count()
#         if items > 0:
#             return Response({"details":"category cannot be deleted. Protected in OrderItem"})
#         category.delete()
#         return Response({"details":"Category deleted successfully"})      
    
#     #table   
# class TableGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Table.objects.all()
#     serializer_class = TableSerializer
    
#     def get(self,request):
#         return self.list(request)       
        
#     def post(self, request):
#         return self.create(request)
        
# class TableDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Table.objects.all()
#     serializer_class = TableSerializer
#     lookup_field = 'id'
#     # (if lookup field use gardina vaneni , we can use pk)
#     def get(self,request,id):       #id = pk rakhni
#         return self.retrieve(request, id)
    
#     def post(self,request,id):
#         return self.update(request, id)

#     def delete(self,request,id):
#         table = Table.objects.get(id = id)
#         table.delete()
#         return Response({"detail": "table deleted successfully"})
    
    

# Mixins kai concrete view classes, genericAPI
# from rest_framework import mixins, generics
 
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# class CategoryGenericAPIView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
# class CategoryDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
#     def delete(self, request,pk):
#         items = OrderItem.objects.filter(food__category = self.get_object).count()
#         if items > 0:
#             return Response({"details":"category cannot be deleted. Protected in OrderItem"})
#         self.get_object().delete()
#         return Response({"details":"Category deleted successfully"})
    


# Class Based: APIView
# from rest_framework.views import APIView

# class CategoryAPIView(APIView):
#     def get(self, request):
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many = True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = CategorySerializer(data = request.data)    #deserialize: json format convert to model instance
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# class CategoryDetail(APIView):
#     def get(self, request, id):
#         category = Category.objects.get(id = id)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data) 
#     def post(self, request, id):
#         category = Category.objects.get(id = id)
#         serializer = CategorySerializer(category, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self, request, id):
#         category =  Category.objects.get(id = id)
#         items = OrderItem.objects.filter(food__category = category).count()
#         if items > 0:
#             return Response({"details":"category cannot be deleted. Protected in OrderItem"})
#         category.delete()
#         return Response({"details":"Category deleted successfully"})
    
     
# class TableAPIView(APIView):
#     def get(self, request):
#         table = Table.objects.all()
#         serializer = TableSerializer(table, many= True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = TableSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    

# class TableDetail(APIView):
#     def get(self, request, id):
#         table = Table.objects.get(id = id)
#         serializer = TableSerializer(table)
#         return Response(serializer.data)
        
#     def push(self, request, id):
#         table = Table.objects.get(id = id)
#         serializer = TableSerializer(table, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         table = Table.objects.get(id = id)
#         table.delete()
#         return Response({"detail": "table deleted successfully"})
        
# Function-based: api_view()

# @api_view(['GET','POST'])
# def category(request):
#     if request.method == 'GET':
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)    #serialize: to convert queryset to json format
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CategorySerializer(data = request.data)    #deserialize: json format convert to model instance
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
# @api_view(['GET','POST','DELETE'])
# def category_detail(request, id):
#     category = Category.objects.get(id = id)
#     if request.method == 'GET':
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CategorySerializer(category, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         items = OrderItem.objects.filter(food__category = category).count()
#         if items > 0:
#             return Response({"detail":"category cannoy be deleted. Protected in OrderItem"})
#         category.delete()
#         return Response({"detail": "Category deleted successfully"})
    
    
# @api_view(['GET','POST'])
# def table(request):
#     if request.method == 'GET':
#         table = Table.objects.all()
#         serializer = TableSerializer(table, many=True)    #serialize: to convert queryset to json format
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TableSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
# @api_view(['GET','POST'])
# def table_detail(request, id):
#     table = Table.objects.get(id = id)
#     if request.method == 'GET':
#         serializer = TableSerializer(table)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TableSerializer(table, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
        


        