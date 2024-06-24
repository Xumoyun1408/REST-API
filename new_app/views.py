from django.shortcuts import render
from django.http import HttpResponse 
from django.forms.models import model_to_dict

from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.request import Request 

from .models import Cars
from .serializers import CarsSerializer

def index(request):
    return HttpResponse('<h1>LINK : 127.0.0.1:8000/api/v1/cars/ </h1>')

class CarsAPIView(APIView):
    def get(self, request: Request):
        cars = Cars.objects.values()
        return Response({'cars': cars})
    
    def post(self, request: Request):
        car = Cars.objects.create(
            name=request.data['name'],
            model=request.data['model'],
            engine=request.data['engine'],
            price=request.data['price'],
            published=request.data['published'],
        )
        return Response(model_to_dict(car))


class CarsAPIDetail(RetrieveAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer                                                                                               