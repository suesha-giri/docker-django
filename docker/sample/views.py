from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def example(request):
    return HttpResponse("This is the docker-django project")
