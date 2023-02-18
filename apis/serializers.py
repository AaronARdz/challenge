from rest_framework import serializers
from zipcodes.models import Zipcode

class ZipcodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zipcode
        fields = ("zip_code", "locality", "settlement", "locality")