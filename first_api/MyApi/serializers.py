from rest_framework import fields, serializers
from .models import Customers

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'