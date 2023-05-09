import json
from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request --> HttpRequest -> Django 
    # print(dir(request))
    # request.body
    body = request.body # byte string of JSON data
    data = {}
    try: 
        data = json.loads(body) # string of JSon data -> python dictionary
    except:
        pass
    print(data)
    # data['headers'] = request.headers # request.META -> older versions of Django
    print(request.headers)
    json.dumps(dict(request.headers))
    data['content_type'] = request.content_type
    return JsonResponse(data)
