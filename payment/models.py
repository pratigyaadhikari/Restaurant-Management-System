from django.db import models
from rms.models import Order
# Create your models here.
class Payment(models.Model):
    PAYMENT_METHOD = [
        ('C', 'Cash'),
        ('K','Khalti'),
        ('E','Esewa'),
        ('F','Fonepay')
    ]
    # order = models.ForeignKey(Order,on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    payment_method = models.CharField(max_length=1,choices=PAYMENT_METHOD)
    pidx = models.CharField(max_length=22, unique=True)
    transaction_id = models.CharField(max_length=100, null=True, blank = True)
    total_amount = models.FloatField()
    status = models.CharField(max_length=15, default='Pending')
    
    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.order.user} - {self.order.status}"