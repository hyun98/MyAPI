from django.urls import path
from accountapp.views import *

app_name = 'accountapp'

urlpatterns = [
    path('register/', RegistrationAPI.as_view(), name="register"),
    path('login/', LoginAPI.as_view(), name="login"),
    path('user/', UserAPI.as_view(), name="userapi"),
    path('showuser/', ShowUser, name="show"),
    path('idcheck/', AccountIDCheck, name="idcheck"),

]