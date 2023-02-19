from django.shortcuts import render

# Create your views here.
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from zipcodes.models import Zipcode
from .serializers import ZipcodeSerializer
# Serializer translates complex data like querysets and model instances into a format
# that is easy to consume over the internet, typically JSON. It is also possible to “deserialize” data,

no_zipcodes_found_msg = 'No zipcodes found'

class ZipCodeAPIView(generics.ListAPIView):
    serializer_class = ZipcodeSerializer
    def get_queryset(self):
        zipcode_number = self.kwargs['zipcode']
        queryset = Zipcode.objects.filter(zip_code=zipcode_number)

        return queryset

class ZipcodeViewSet(APIView):

    def handle_data(self,results):
        settlement_list = []
        federal_entity = dict(
            key=results[0].federal_entity_key,
            name=results[0].federal_entity,
            code=results[0].federal_entity_code
        )

        municipality = dict(
            key=results[0].municipality_code,
            name=results[0].municipality,
        )

        for result in results:
            settlement_type_dict = dict(name = result.settlement_type)
            settlement = dict(
                key=result.settlement_code,
                name=result.settlement,
                zone_type=result.zone_type,
                settlement_type =settlement_type_dict
            )
            settlement_list.append(settlement)

        response_obj = dict(
            locality=results[0].locality,
            zip_code=results[0].zip_code,
            settlement=settlement_list,
            federal_entity=federal_entity,
            municipality=municipality
        )

        return response_obj


    def get(self, request, zipcode):
        zipcode_number = self.kwargs['zipcode']

        try:
            queryset = Zipcode.objects.filter(zip_code=zipcode_number)
        except Zipcode.DoesNotExist:
            return Response(
                {
                    'Data': []
                },
                status=status.HTTP_400_BAD_REQUEST)

        result_list = list(queryset.all())

        if len(result_list) == 0:
            return Response(
                {
                    'Data': [],
                    'message': no_zipcodes_found_msg
                },
                status=status.HTTP_204_NO_CONTENT)

        response = self.handle_data(results=result_list)


        return Response({'Data': response}, status=status.HTTP_200_OK)