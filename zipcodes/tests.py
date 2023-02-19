from django.test import TestCase
from .models import Zipcode

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.Zipcode = Zipcode.objects.create(
                zip_code="641203",
                locality="Monterrey",
                settlement="Churubusco",
                settlement_type="Colonia",
                settlement_code=22,
                zone_type='rural',
                municipality='Monterrey',
                municipality_code=39,
                federal_entity='Nuevo Leon',
                federal_entity_key=19,
                federal_entity_code=0

        )

    def test_zipcode_content(self):
        self.assertEqual(self.Zipcode.zip_code, '641203')
        self.assertEqual(self.Zipcode.locality, 'Monterrey')
        self.assertEqual(self.Zipcode.settlement, 'Churubusco')
        self.assertEqual(self.Zipcode.settlement_type, 'Colonia')
        self.assertEqual(self.Zipcode.settlement_code, 22)
        self.assertEqual(self.Zipcode.zone_type, 'rural')
        self.assertEqual(self.Zipcode.municipality, 'Monterrey')
        self.assertEqual(self.Zipcode.municipality_code, 39)
        self.assertEqual(self.Zipcode.federal_entity, 'Nuevo Leon')
        self.assertEqual(self.Zipcode.federal_entity_key, 19)
        self.assertEqual(self.Zipcode.federal_entity_code, 0)
