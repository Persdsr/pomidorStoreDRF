from django.shortcuts import render
from .models import SalesOrder
from .serializers import OrderSerializer

from rest_framework.viewsets import ModelViewSet


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer


def orders_app(request):
    return render(request, 'orders/main_app.html')