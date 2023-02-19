# apis/urls.py
from django.urls import path,register_converter

from .views import ZipCodeAPIView,ZipcodeViewSet
from . import converter

register_converter(converter.FiveDigitZipcode, 'nnnnn')

urlpatterns = [
    path("test/<int:zipcode>", ZipCodeAPIView.as_view(), name="zipcode_list"),
    path("zipcodes/<int:zipcode>", ZipcodeViewSet.as_view(), name='xd')
]