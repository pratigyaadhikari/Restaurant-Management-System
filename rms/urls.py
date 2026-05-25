from django.urls import path
from .views import category,table


urlpatterns = [
    path('category/', category),
    path('table/', table)
]
