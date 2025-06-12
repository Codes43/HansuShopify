from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .user_model import CustomUserManager


# Adding a product model
class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to="products/")


#User model
class CustomUSer(AbstractUser):
    email = models.EmailField(_('email address'), unique=True) # Make sure this has unique=True
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager() 

    

    def __str__(self):
        return self.email
    
    


