from django.contrib import admin
from .models import * 


class OrderAdmin(admin.ModelAdmin):
    list_display=['fname','payment_id','item']
# Register your models here.
admin.site.register(Order,OrderAdmin)
