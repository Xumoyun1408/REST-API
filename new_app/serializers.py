from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io

from .models import Cars

class Cars:
    def __init__(self, name, model, engine, price):
        self.name = name
        self.model = model
        self.engine = engine
        self.price = price
    
cars_object_1 = Cars(name="eshak", model="Chevrolete", engine="1", price=1000000)


class CarsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    engine = serializers.IntegerField()
    price = serializers.FloatField()

def serialization():
    print(cars_object_1)
    serializer = CarsSerializer(cars_object_1)
    print(serializer.data)
    json = JSONRenderer().render(serializer.data)
    print(json)

def deserialization():
    json = b'{"name":"eshak","model":"Chevrolete","engine":1,"price":1000000.0}'
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    print(data)
    serializer = CarsSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)