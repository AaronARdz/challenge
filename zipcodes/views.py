from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Zipcode
import pandas as pd
import lxml

def run():
    df = pd.read_xml('Codigos.xml')
    df = df.drop(['targetNamespace', 'elementFormDefault', 'import', 'element'], axis=1)

    results = df.to_dict('records')

    model_instances = [Zipcode(
        zip_code=record['d_codigo'],
        locality=record['d_ciudad'],
        settlement=record['d_asenta'],
        settlement_type=record['d_tipo_asenta'],
        settlement_code=record['id_asenta_cpcons'],
        zone_type=record['d_zona'],
        municipality=record['D_mnpio'],
        municipality_code=record['c_mnpio'],
        federal_entity=record['d_estado'],
        federal_entity_key=record['c_estado'],
        federal_entity_code=record['c_CP'],
    ) for record in results]

    Zipcode.objects.bulk_create(model_instances)

    return 0

class ZipcodeListView(ListView):
    model = Zipcode
    template_name = "zipcode_list.html"

   # Read all existing records of books table
    queryset = Zipcode.objects.all()
    print(queryset.count())
    # Check the books table is empty or not
    if queryset.count() < 2:
        run()

    # Return all records of the books table
    def get_queryset(self):
        # Set the default query set
        return Zipcode.objects.all()

