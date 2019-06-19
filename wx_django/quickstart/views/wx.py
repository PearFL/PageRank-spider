from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse, FileResponse
from JuheApi import weatherApi
import json
import utils.response

def helloworld(request):
    print('request method:', request.method)
    print('request META:', request.META)
    print('request cookies:', request.COOKIES)
    print('request QueryDict: ', request.GET)
    # return HttpResponse(content='Hello Django Response', status=201)
    search = request.GET.get('search')
    m = [{
        "url": "http://www.hfuu.edu.cn/",
        "title": search,
        "in": 35,
        "out": 27,
        "pg": 4.9,
        "rank": 12
    }, {
        "url": "http://www.hfuu.edu.cn/jwc/",
        "title": "教务处",
        "in": 22,
        "out": 31,
        "pg": 3.2,
        "rank": 8
    },
    ]
    response = utils.response.wrap_json_response(data=m,
                                                 code=utils.response.ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False, status=200)


def weather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        data = weatherApi.weather(city)
        return JsonResponse(data=data, safe=False, status=200)
    elif request.method == 'POST':
        received_body = request.body
        received_body = json.loads(received_body)
        cities = received_body.get('cities')
        response_data = []
        for city in cities:
            result = weatherApi.weather(city)
            result['city'] = city
            response_data.append(result)
        return JsonResponse(data=response_data, safe=False, status=200)


def pagerank(request):
    if request.method == 'GET':
        search = request.GET.get('search')

        response = utils.response.wrap_json_response(data=search,
                                                     code=utils.response.ReturnCode.SUCCESS)
        return JsonResponse(data=response, safe=False, status=200)