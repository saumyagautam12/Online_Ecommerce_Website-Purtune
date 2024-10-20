from django.db import models
from core.models import CustomUser

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    category=models.ForeignKey(Category,related_name="items",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    price=models.FloatField()
    image=models.ImageField(upload_to="items_images",blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(CustomUser,related_name='items',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




