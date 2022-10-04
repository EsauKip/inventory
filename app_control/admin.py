from django.contrib import admin
from.models import Inventory,InventoryGroup
# Register your models here.
admin.site.register((Inventory,InventoryGroup,))