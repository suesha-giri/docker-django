from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomersSerializer
from .models import Customers
from django.db.models import Count

@api_view(['GET']) #decorators
def api(request):
    return Response("I am the API endpoint.")

@api_view(['GET'])
def count(request):
    total_customers= Customers.objects.count()
    return Response({'The number of customers are': total_customers})

@api_view(['GET'])
def dbList(request):
    db=Customers.objects.all()
    serializer = CustomersSerializer(db, many='True')
    return Response(serializer.data)

