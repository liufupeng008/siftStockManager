from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from  stockInfo.models import StockInfo
# Create your views here.
import json
import os
@login_required()
def addList(request):
    stockDataPath = os.getcwd()+'/stockData/'
    print(stockDataPath)
    import csv
    includes = ['sexchange', 'scode', 'scompany_name', 'sindustry',
                             'spe_ttm', 'spb', 'sdividend_yield', 'sstock_prices', 'spb_ten_year']
    # 'spe_sort', 'spb_sort', 'sdividend_yield_sort', 'synthetical_sort'
    spe_sort_list = list()
    spb_sort_list = list()
    sdividend_yield_sort = list()
    synthetical_sort = list()

    if os.path.exists(stockDataPath):
        for root, dirs, files in os.walk(stockDataPath):
            _files = list(filter(lambda x: x.endswith('.csv'), files))
            for _csv in _files:
                with open(stockDataPath+_csv, "r") as csvfile:
                     reader = csv.reader(csvfile)
                     for idx, line in enumerate(reader):
                         if idx == 0:
                             continue
                         stocklist = list(line)
                         if len(stocklist) == 9:

                            spe_idx = includes.index('spe_ttm')
                            spe_sort_list.append(float(stocklist[spe_idx]))

                            spb_idx = includes.index('spb')
                            spb_sort_list.append(float(stocklist[spb_idx]))

                            sdividend_yield_idx = includes.index('sdividend_yield')
                            sdividend_yield_sort.append(float(stocklist[sdividend_yield_idx]))

                     bubble_sort(spe_sort_list)
                     bubble_sort(spb_sort_list)
                     bubble_sort(sdividend_yield_sort)
                     for idx,line in enumerate(reader):
                         if idx == 0:
                             continue
                         stocklist = list(line)
                         if len(stocklist)==9:
                             scode = stocklist[1]
                             scode = scode.replace('"', '')
                             scode = scode.replace('=', '')
                             stocklist[1] = scode
                             stock = StockInfo()
                             oldstock = StockInfo()
                             for i, data in enumerate(stocklist):
                                 property = includes[i]
                                 setattr(stock, property, data)
                             try:
                                oldstock = StockInfo.objects.get(scode=scode)
                                if oldstock:
                                    stock.id = oldstock.id
                                    stock.spe
                                    stock.save(force_update=True)
                             except (oldstock.DoesNotExist)as e:
                                    stock.save()
                                    print(stock.prn_obj())
    data = {'code': 0,

            'error': os.getcwd(),
            'msg': '打包过程中出错'}
    # return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, 'home.html', {})


@login_required()
def home(request):
    return render(request, 'home.html', {})


@login_required()
def test(request):
    pass


def bubble_sort(arr):
    length = len(arr)
    while length > 0:
        for i in range(length - 1):
            if arr[i] - arr[i + 1]>0.01:
                arr[i] = arr[i] + arr[i + 1]
                arr[i + 1] = arr[i] - arr[i + 1]
                arr[i] = arr[i] - arr[i + 1]
        length -= 1

