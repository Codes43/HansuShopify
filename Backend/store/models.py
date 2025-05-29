from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .user_model import CustomUserManager
# Create your models here.



class CustomUSer(AbstractUser):
    email = models.EmailField(_('email address'), unique=True) # Make sure this has unique=True
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager() 

    

    def __str__(self):
        return self.email
    
    


