from django.contrib import admin

# Register your models here.
from .models import Book, Zipcode

admin.site.register(Book)
admin.site.register(Zipcode)
