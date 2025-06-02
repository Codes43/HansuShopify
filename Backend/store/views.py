from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import ProductSerializer,UserSerializer,SignUpSerializer
from .models import Product


##import of generic views
from rest_framework import generics

##  This view is simplily for listing all products from the database or create a new product

class CreateProductView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class ListProductsView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field="pk"
class UpdateProductView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field="pk"
class DeleteProductView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field="pk"




### handle User Management
def get_auth_for_user(user):
    # tokens=RefreshToken(user)
    # print(tokens)
    return{
        'user':UserSerializer(user).data,
        #  'tokens': {
        #      'access':str(tokens.access_token),
        #      'refresh':str(tokens)
        # }
    }



class SignInView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        # username=request.data.get('username')
        email=request.data.get('email')
        password=request.data.get('password')

        ## handle invalid credentials
        if not email and not password:
            return Response(status=400)
        
        user=authenticate(email=email,password=password)
        ##if the user isn,t authorized
        if not user:
            return Response(status=401)
        user=get_auth_for_user(user)

        return Response(user)

   

class SignUpView(APIView):
    permission_classes=[AllowAny]

    def post(self,request):
        new_user= SignUpSerializer(data=request.data)
        new_user.is_valid(raise_exception=True)
        user=new_user.save()
        #we shall grab the token and return the newly created user data
        user_data=get_auth_for_user(user)
        return Response(user_data)