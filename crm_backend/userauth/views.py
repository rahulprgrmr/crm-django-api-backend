from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import AuthTokenSerializer

# Create your views here.

class LoginView(ObtainAuthToken):
    serializer_class=AuthTokenSerializer