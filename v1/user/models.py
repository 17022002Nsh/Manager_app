from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from v1.home.models import  DefaultAbstract
from v1.user.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin, DefaultAbstract):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.first_name}, {self.phone}"
    
    
    
    objects = UserManager()

   
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
   
    
    

    
    
    
    
    
    
    
