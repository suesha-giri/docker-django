
from rest_framework.response import Response
from .serializers import CustomersSerializer
from .models import Customers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from MyApi import serializers


class ApiView(APIView):
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        content ={"message": "I am the endpoint"}

        return Response(content)

class CountView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        total_customers= Customers.objects.count()

        return Response({'The number of customers are': total_customers})


class DblistView(APIView):

    def get(self, request):
        db= Customers.objects.all()
        serializer= CustomersSerializer(db, many='True')

        return Response(serializer.data)


