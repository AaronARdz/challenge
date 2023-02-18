# apis/urls.py
from django.urls import path

from .views import ZipCodeAPIView

urlpatterns = [
    path("", ZipCodeAPIView.as_view(), name="zipcode_list"),
]

