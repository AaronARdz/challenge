from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from zipcodes.models import Zipcode
from .serializers import ZipcodeSerializer
# Serializer translates complex data like querysets and model instances into a format
# that is easy to consume over the internet, typically JSON. It is also possible to “deserialize” data,

class ZipCodeAPIView(generics.ListAPIView):
    queryset = Zipcode.objects.filter(zip_code = "")
    serializer_class = ZipcodeSerializer
