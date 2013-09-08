from django.utils import simplejson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from apps.products.models import Product

import json


@csrf_exempt
def get_or_create(request):
    context = {}

    if request.method == "GET":
        print "GET"

    if request.method == "POST":
        data = json.loads(request.body).get('product')
        product = Product.objects.create(**data)
        context = {
            "id": product.id,
            "name": product.name,
            "quantity": product.quantity,
            "limit": product.limit
        }

    

    response = HttpResponse(simplejson.dumps(context), mimetype='application/json')
    return response


def get(request, id):
    product = Product.objects.get(id=id)
    context = {
        "id": product.id,
        "name": product.name,
        "quantity": product.quantity,
        "limit": product.limit
    }
    response = HttpResponse(simplejson.dumps(context), mimetype='application/json')
    return response