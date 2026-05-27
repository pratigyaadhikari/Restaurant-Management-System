from django.urls import path
from .views import category,table, category_detail, table_detail


urlpatterns = [
    path('category/', category),
    path('category/<id>/', category_detail),
    path('table/', table),
    path('table/<id>/', table_detail)
]
