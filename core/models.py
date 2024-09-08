from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from .manager import *

from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from multiselectfield import MultiSelectField

# Create your models here.
class CustomUser(AbstractBaseUser,PermissionsMixin):

    # username=None
    email=models.EmailField(unique=True)     
    #  class attributes ->
    Name=models.CharField(max_length=100,blank=True)
    # lastlogin=models.DateTimeField()   already in AbstractBaseUser
    date_joined=models.DateTimeField(default=timezone.now)
    is_staff =models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    type=(
        (1,"Seller"),
        (2,"Customer")
    )
    # default_type=2

    
    default_type=2
    # user_type=models.IntegerField(choices=type,default=root)
    user_type=MultiSelectField(choices=type,
                                 default=[],
                                 null=True,blank=True)
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[] 

    objects=CustomUserManager()

    def __str__(self):
        return self.Name

    def save(self,*args,**kwargs):
        if not self.id:
            # self.user_type=self.default_type

            self.user_type.append(self.default_type)
        
        return super().save(*args,**kwargs)


class CustomerManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(Q(user_type__contains=CustomUser.default_type))
            
            # user_type=2)



class SellerManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(Q(user_type__contains=CustomUser.default_type))




class Customer(CustomUser):
    # CustomUser.user_type=2
    # user_type=CustomUser.user_type
    default_type=2
    
    objects=CustomerManager()

    class Meta:
        proxy=True

    @property
    def showAdditional(self):
        return self.customeradditional
    



    # user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    # address=models.CharField(max_length=150)
# 

class Seller(CustomUser):
    # CustomUser.user_type=1
    # user_type=CustomUser.user_type
    default_type=1
    
    objects=SellerManager()

    class Meta:
        proxy=True

    @property
    def showAdditional(self):
        return self.selleradditional






class CustomerAdditional(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)

class SellerAdditional(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gst=models.CharField(max_length=10)
    warehouse=models.CharField(max_length=100)

