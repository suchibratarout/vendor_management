from django.contrib import admin
from .models import Vendor
from .models import PurchaseOrder
# Register your models here.
admin.site.register(Vendor)
admin.site.register(PurchaseOrder)