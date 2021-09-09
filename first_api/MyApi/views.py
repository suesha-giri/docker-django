from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api(request):
    return Response("I am the API endpoint.")
