import math

from django.views.generic import ListView
from .models import Zipcode
import pandas as pd
import lxml

def load_data():
    df = pd.read_xml('Codigos.xml')
    df = df.drop(['targetNamespace', 'elementFormDefault', 'import', 'element'], axis=1)

    results = df.to_dict('records')
    model_instances = []

    for record in results:
        if math.isnan(record['d_codigo']):
            continue

        instance = Zipcode()
        instance.zip_code = int(record['d_codigo'])
        instance.locality = record['d_ciudad']
        instance.settlement = record['d_asenta']
        instance.settlement_type = record['d_tipo_asenta']
        instance.settlement_code = 0 if math.isnan(record['id_asenta_cpcons']) else int(record['id_asenta_cpcons'])
        instance.zone_type = record['d_zona']
        instance.municipality = record['D_mnpio']
        instance.municipality_code = 0 if math.isnan(record['c_mnpio']) else int(record['c_mnpio'])
        instance.federal_entity = record['d_estado']
        instance.federal_entity_key = 0 if math.isnan(record['c_estado']) else int(record['c_estado'])
        instance.federal_entity_code = 0 if math.isnan(record['c_CP']) else int(record['c_CP'])

        model_instances.append(instance)

    Zipcode.objects.bulk_create(model_instances)

    return 0

class ZipcodeListView(ListView):
    model = Zipcode
    template_name = "zipcode_list.html"

   # Read all existing records of books table
    queryset = Zipcode.objects.all()
    # Check the books table is empty or not
    if queryset.count() < 2:
        load_data()

    # Return all records of the books table
    def get_queryset(self):
        # Set the default query set
        return Zipcode.objects.all()

