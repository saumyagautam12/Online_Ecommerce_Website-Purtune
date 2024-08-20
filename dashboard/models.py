from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
import datetime


from Item.models import * 

class Order(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100,default='')
    lname=models.CharField(max_length=100,default='')
    phone=models.CharField(max_length=10,default='')
    address=models.CharField(max_length=100,default='',null=False)
    city=models.CharField(max_length=100,default='')
    state=models.CharField(max_length=100,default='')
    pincode=models.CharField(max_length=100,default='')
    payment_id=models.CharField(max_length=100,default='')
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
   
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    status=models.BooleanField(default=False)
    date=models.DateField(default=datetime.datetime.today) 


    def __str__(self):
        return self.payment_id





# Create your models here.

# class Category(models.Model):
#     name=models.CharField(max_length=50)

#     def __str__(self):
#         return self.name


# class Item(models.Model):
#     category=models.ForeignKey(Category,related_name="items",on_delete=models.CASCADE)
#     name=models.CharField(max_length=100)
#     description=models.CharField(max_length=500)
#     price=models.FloatField()
#     image=models.ImageField(upload_to="items_images",blank=True,null=True)
#     is_sold=models.BooleanField(default=False)
#     created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
#     created_at=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
