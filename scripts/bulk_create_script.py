import pandas as pd
import lxml
from zipcodes.models import Zipcode


def run():
    df = pd.read_xml("Codigos.xml")
    df = df.drop(['targetNamespace', 'elementFormDefault', 'import', 'element'], axis=1)

    results = df.to_dict('records')

    model_instances = [Zipcode(
        zip_code=record['d_codigo'],
        locality=record['d_ciudad'],
        settlement=record['d_acenta'],
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


if __name__ == '__main__':
    run()