from rest_framework import serializers
from .models import CustomUSer, Product,Category

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name']



class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True               
    )
    class Meta:
        model=Product
        fields = ['id', 'name', 'description', 'price', 'image', 'category','category_id']
    def get_imageUrl(self, obj):
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