from django.urls import path, include
from rest_framework import routers

from stockapp.views import *

app_name = 'stockapp'

router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path('company/', getCompanylist),
    path('data/<str:name>', getCompanyDataAll),
    path('testi/', TestView.as_view()),
    path('testk/', Testk),
    path('update/', UpdateTest.as_view()),
    
]