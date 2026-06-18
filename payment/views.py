from django.shortcuts import render
from rest_framework.views import APIView
from rms.models import Order
import json, requests
from django.conf import settings
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# initiate garna ko lagi

class PaymentAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        order_id = request.data.get("order_id")
        order = Order.objects.get(id = order_id, user = request.user)
        payload = json.dumps({
            "return_url": "http://127.0.0.1:8000/payment-success/",
            "website_url": "http://127.0.0.1:8000/",
            "amount": order.total_price * 100,
            "purchase_order_id": str(order.id),
            "purchase_order_name": f"Order {order.id}",
        })
        
        headers = {
            'Authorization': f'key {settings.KHALTI_SECRET_KEY}',
            'Content-Type': 'application/json',
        }
        
        response = requests.request("POST", settings.KHALTI_INITIATE_URL, headers=headers, data=payload)

        data = response.json()   
        
        Payment.objects.create(
            order = order,
            pidx = data.get('pidx'),
            total_amount = order.total_price,
            status = "Pending"
        )
        
        return Response(data)
                
                
      # verification  
class PaymentVerifyAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        pidx = request.data.get("pidx")
        
        headers = {
                'Authorization': f'key {settings.KHALTI_SECRET_KEY}',
                'Content-Type': 'application/json',
            }
        response = requests.request("POST",url = settings.KHALTI_LOOKUP_URL, json={"pidx":pidx}, headers=headers)
        data = response.json()
        payment = Payment.objects.get(pidx = pidx)
        if data.get('status')=="Completed":
            payment.status = "Completed"
            payment.transaction_id  = data.get('transaction_id')
            payment.order.payment_status = "C"
            payment.order.save()
        payment.save()
        return Response(data)
        
        
