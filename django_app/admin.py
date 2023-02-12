from django.contrib import admin
from .models import Site, IAP, Switch, Order

# Register your models here.

admin.site.register(Site)
admin.site.register(IAP)
admin.site.register(Switch)
admin.site.register(Order)