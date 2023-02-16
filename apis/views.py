from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer
# Serializer translates complex data like querysets and model instances into a format
# that is easy to consume over the internet, typically JSON. It is also possible to “deserialize” data,

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
