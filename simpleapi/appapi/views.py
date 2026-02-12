from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def product_list(request):
    products = [
        {"name": "Laptop", "price": 50000, "category": "Electronics"},
        {"name": "Shoes", "price": 2500, "category": "Fashion"},
        {"name": "Watch", "price": 3000, "category": "Accessories"},
    ]
    return Response(products, status=HTTP_200_OK)
