from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Table, OrderItem
from .serializer import CategorySerializer, TableSerializer


# Create your views here.
# Mixins:
from rest_framework import mixins, generics

class CategoryGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get(self,request):
        return self.list(request)       #if useing mixin yo line matra lekhda vo insted of mathi ko 3 ota line code
        
        # category = Category.objects.all()
        # serializer = CategorySerializer(category, many = True)
        # return Response(serializer.data)
        
    def post(self, request):
        return self.create(request)
    
    
    
class CategoryDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
    # (if lookup field use gardina vaneni , we can use pk)
    def get(self,request,id):       #id = pk rakhni
        return self.retrieve(request, id)
    
    
   





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
    
        


        