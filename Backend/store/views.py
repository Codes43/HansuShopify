from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
##import the simple jwt to handle tokens
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
from django.contrib.auth import authenticate
from .serializers import UserSerializer 

def get_auth_for_user(user):
    # tokens=RefreshToken(user)
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

   

