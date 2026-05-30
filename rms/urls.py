from django.urls import path
# from .views import category,table, category_detail, table_detail
# from .views import CategoryAPIView, CategoryDetail, TableAPIView, TableDetail
from .views import CategoryGenericAPIView, CategoryDetail, TableGenericAPIView, TableDetail
urlpatterns = [
    # Mixins:
    path("category/", CategoryGenericAPIView.as_view()),
    path("category/<pk>/", CategoryDetail.as_view()),    #esma ni id ko satta pk rakhni
    path('table/', TableGenericAPIView.as_view()),
    path('table/<id>/',TableDetail.as_view())
    ]
    
    
    # Class Based:
    # path('category/', CategoryAPIView.as_view()),
    # path('category/<id>/', CategoryDetail.as_view()),
    # path('table/', TableAPIView.as_view()),
    # path('table/<id>/',TableDetail.as_view())
    
    
    
    
    # function based:
    # path('category/', category),
    # path('category/<id>/', category_detail),
    # path('table/', table),
    # path('table/<id>/', table_detail)

