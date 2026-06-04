from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.

class LoginViewset(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user  = authenticate(username=username, password=password)      #verification lai send gareko using authenticate
        if user:
            token,_ = Token.objects.get_or_create(user=user)
            return Response({"token":token.key,"username":username})
        else:
            return Response({"detail":"User does not exists."})    




# token authentication ko kam garda install proces sakesi migrate file create garnu parxa, DRF file ma hera steps ko lagi.




# - user post username, password
# - verify username and password
# - if valid, generate token and send to user