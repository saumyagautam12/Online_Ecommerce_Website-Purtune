from django.contrib import admin

# Register your models here.
from Item.models import * 

admin.site.register(Category)
admin.site.register(Item)