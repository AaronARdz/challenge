# apis/urls.py
from django.urls import path,register_converter

from .views import ZipcodeViewSet
from . import converter

register_converter(converter.FiveDigitZipcode, 'nnnnn')

urlpatterns = [
    path("zipcodes/<int:zipcode>", ZipcodeViewSet.as_view(), name='zipcode_list')
]