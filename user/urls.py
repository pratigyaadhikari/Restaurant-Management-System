from django.urls import path

from .views import *

urlpatterns = [
    path('login/',LoginViewset.as_view(),name='login')
]
