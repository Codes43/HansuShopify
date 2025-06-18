from rest_framework import serializers
from .models import CustomUSer, Product,category

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = category
        fields = ['id', 'name']



class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
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
        model = CustomUSer
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        email = validated_data['email'].lower().strip()  # Normalize email
        password = validated_data['password']
        
        user = CustomUSer.objects.create_user(  # Use create_user instead of create
            email=email,
            password=password  # This will handle hashing automatically
        )
        return user

#  def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         return super().create(validated_data)