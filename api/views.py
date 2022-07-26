import json
from wsgiref import headers
# from django.http import HttpResponse, JsonResponse, HttpResponse
from django.forms.models import model_to_dict
# from yaml import serialize
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
# Create your views here.x


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id', 'price', 'title', 'sale_price',])
        data = ProductSerializer(instance).data
    return Response(data)

