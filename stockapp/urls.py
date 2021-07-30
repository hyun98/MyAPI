from django.urls import path, include
from rest_framework import routers

from stockapp.views import *

app_name = 'stockapp'

router = routers.DefaultRouter()
# router.register(r'kospi/',KospiAPIView.as_view())
# router.register(r'chart/',ChartView.as_view())

urlpatterns = [
    # path('kospi/', kospi_list, name='kospilist'),
    # path('kospi/<int:pk>', kospi_detail, name='kospidetail'),
    path('', include(router.urls)),
    path('stock/', StockAPIView.as_view()),
    path('chart/', ChartView.as_view()),
    path('data/', getStockDataAll),
    path('company/', getCompanylist),
    path('data/<str:name>', getCompanyDataAll),
    
]