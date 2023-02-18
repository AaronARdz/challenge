# zipcodes/urls.py
from django.urls import path

from .views import ZipcodeListView
urlpatterns = [
    path("", ZipcodeListView.as_view(), name="home"),
]
