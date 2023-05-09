import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework import Response

from products.models import Product

@api_view
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
       data = model_to_dict(model_data), fields=['id', 'title']

    return Response(data)
    # return JsonResponse(data)   