from rest_framework import serializers
from .models import *




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CustomUSer
        fields=[
            'username',
            'email',
            'first_name',
            'last_name'
        ]
            
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUSer
        fields=[
            'email',
            'password'
        ]
        
        extra_kwargs={
            'password':{
              'write_only':True
            }
        }
        def create(self,validate_data):
            email=validate_data['email'].lower()
            user =CustomUSer.objects.create(
                email=email
            )
            password=validate_data['password']
            user.set_password(password)
            user.save()
            return user

