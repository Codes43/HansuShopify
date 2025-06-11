from rest_framework import serializers
from .models import CustomUSer, Product




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

    def get_imageUrl(self, obj):
        # This correctly forms the absolute URL for the image
        if obj.image:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url # Fallback if request context isn't available
        return 

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CustomUSer
        fields=[
            'id',
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

