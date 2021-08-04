from django.urls import path, include
from rest_framework import routers

from stockapp.views import *

app_name = 'stockapp'

router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    # path('stock/', StockAPIView.as_view()),
    # path('chart/', ChartView.as_view()),
    # path('data/', getStockDataAll),
    path('company/', getCompanylist),
    path('data/<str:name>', getCompanyDataAll),
    
]