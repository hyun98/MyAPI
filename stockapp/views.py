from abc import get_cache_token
from config.settings.base import MEDIA_ROOT
from time import strptime, mktime
import json

from rest_framework.decorators import api_view
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.middleware.csrf import get_token

from stockapp.models import Company, StockInfo


def getdata(stocks):
    close_list = []
    open_list = []
    low_list = []
    high_list = []
    vol_list = []

    for stock in stocks:
        times = strptime(str(stock.date), '%Y-%m-%d')
        utc_now = mktime(times) * 1000

        close_list.append([utc_now, stock.close, stock.id])
        open_list.append([utc_now, stock.open, stock.id])
        high_list.append([utc_now, stock.high, stock.id])
        low_list.append([utc_now, stock.low, stock.id])
        vol_list.append([utc_now, stock.volume, stock.id])

    data = {
        'close': close_list,
        'open': open_list,
        'high': high_list,
        'low': low_list,
        'vol': vol_list,
    }
    return data


def getStockDataAll(request):
    stocks = StockInfo.objects.all().order_by('date')
    data = getdata(stocks)
    return JsonResponse(data)


def getCompanylist(request):
    company = Company.objects.all()
    com_list = []
    for com in company:
        if not com.companyico:
            com_list.append([com.name, "/media/unnamed.gif"])
        else:
            com_list.append([com.name, com.companyico.url])
    
    data = {
        'company': com_list
    }
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def getCompanyDataAll(request, name):
    cid = get_object_or_404(Company, name=name)
    stocks = StockInfo.objects.filter(company__id=cid.id).order_by('date')
    data = getdata(stocks)
    return JsonResponse(data)
    
    
class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html')

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt)
def Testk(request):
    if request.method == 'POST':
        dist = request.POST['dist']
        context = {'dist': dist}
        print("???????????? ???????????????.")
        response = JsonResponse(context)
        
    else:
        context = {
            'dist': 'no data',
        }
        print("???????????? ?????? ???????????????.")
        response = JsonResponse(context)
    
    return response


class UpdateTest(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "message": "Update Complete!! ???????????? ????????? ?????????????"
            }, status=status.HTTP_200_OK)


class TestView(View):
    def get(self, request):
        context = {
            'dist': 'no data',
        }
        response = JsonResponse(context)
        return response
    
    def post(self, request):
        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)
            context = {
                'dist': request['dist'],
            }
        else:
            context = {
                'dist': 'post no data'
            }
        response = JsonResponse(context)
        return response