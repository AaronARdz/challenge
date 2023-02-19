from rest_framework import serializers
from zipcodes.models import Zipcode

settlement_list = []

class ZipcodeSerializer(serializers.ModelSerializer):
    federal_entity = serializers.SerializerMethodField('get_federal_entity')
    municipality = serializers.SerializerMethodField('get_municipality')
    settlements = serializers.SerializerMethodField('get_settlements')

    def get_federal_entity(self, zipcode_object):
        fed_entity = dict(
            key = getattr(zipcode_object, 'federal_entity_key'),
            name = getattr(zipcode_object, 'federal_entity'),
            code = getattr(zipcode_object, 'federal_entity_code')
        )
        return fed_entity

    def get_municipality(self, zipcode_object):
        municipality = dict(
            key = getattr(zipcode_object, 'municipality_code'),
            name = getattr(zipcode_object, 'municipality'),
        )
        return municipality

    def get_settlements(self, zipcode_object):
        global settlement_list

        settlement_type_dict = dict(name = getattr(zipcode_object, 'settlement_type'))
        settlement = dict(
            key = getattr(zipcode_object, 'settlement_code'),
            name = getattr(zipcode_object, 'settlement'),
            zone_type = getattr(zipcode_object, 'zone_type'),
            settlement_type = settlement_type_dict
        )

        settlement_list.append(settlement)
        return settlement_list

    class Meta:
        model = Zipcode
        fields = ('zip_code',
                  'locality',
                  'municipality',
                  'federal_entity',
                  'settlements'
                  )