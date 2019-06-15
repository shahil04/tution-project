from django.contrib import admin
from .models import Products,Address,Consultancy,Contact
from .models import Website_services,Features_add,Train



admin.site.register(Products)
admin.site.register(Address)
admin.site.register(Consultancy)
admin.site.register(Contact)
admin.site.register(Website_services)
admin.site.register(Features_add)
admin.site.register(Train)