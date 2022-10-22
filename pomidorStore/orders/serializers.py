from rest_framework import serializers

from .models import SalesOrder


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = '__all__'
