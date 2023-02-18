from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

class Zipcode(models.Model):
    zip_code = models.IntegerField(null=False) # d_codigo
    locality = models.CharField(max_length=250, null=True) # d_ciudad
    settlement = models.CharField(max_length=100, null=True) # d_acenta
    settlement_type = models.CharField(max_length=20, null=True) # d_tipo_asenta
    settlement_code = models.IntegerField(null=True) # id_asenta_cpcons
    zone_type = models.CharField(max_length=20, null=True) # d_zona
    municipality = models.CharField(max_length=20, null=True) #d mnpio
    municipality_code = models.IntegerField( null=True)  # c mnpio
    federal_entity = models.CharField(max_length=50, null=True) #d_estado
    federal_entity_key = models.IntegerField(null=True) # c_estado
    federal_entity_code = models.IntegerField(null=True) # c_ CP

    def __str__(self):
        return self.zip_code
