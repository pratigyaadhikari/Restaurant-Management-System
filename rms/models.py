from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
class Table(models.Model):
    number = models.CharField(max_length=2)
    capacity = models.CharField(max_length=2)
    is_available = models.BooleanField(default=True)
    
class Order(models.Model):
    STATUS_CHOICE = [
        ('P','Pending'),
        ('C','Complete'),
        ('D','Delivered')    
    ]
    PAYMENT_STATUS = [
        ('P','PAID'),
        ('U','PENDING')
    ]   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='P') 
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default='U') 
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    
class Payment(models.Model):
    PAYMENT_METHOD = [
        ('C', 'Cash'),
        ('K','Khalti'),
        ('E','Esewa'),
        ('F','Fonepay')
    ]
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=1,choices=PAYMENT_METHOD)
 
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    time = models.DateTimeField()
    total_users = models.IntegerField()    