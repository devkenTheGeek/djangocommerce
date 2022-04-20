from django.contrib import admin

# Register your models here.
from store.models import *

admin.site.register(Order)
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Customer)


