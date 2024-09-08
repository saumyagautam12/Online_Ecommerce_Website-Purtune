from django.contrib import admin
from .models import * 
admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(Seller)

admin.site.register(SellerAdditional)
admin.site.register(CustomerAdditional)
# from core.models import * 

# admin.site.register()

# Register your models here.
