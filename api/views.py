from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
import random
from django.core.mail import EmailMultiAlternatives
from api import serializer as api_serializer
from userauths.models import User, Profile
from django.template.loader import render_to_string

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = api_serializer.TokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = api_serializer.RegisterSerializer


def generate_random_otp(length=10):
    otp = ''.join([str(random.randint(0, 9) for _ in range(length))])
    return otp


class PasswordResetEmailVerifyAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = api_serializer.UserSerializer

    def get_object(self):
        email = self.kwargs['email']

        user = User.objects.filter(email=email).first()
        if user:
            uuid64 = user.pk
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh.access_token)
            user.otp = generate_random_otp()
            user.save()
            link = f"http://localhost:3000/create-new-pass/?otp{user.otp}&uuid64={uuid64}"
            context = {
                "link": link,
                "username": user.username
            }
            subject = 'Password Reset Link'
            text_body = render_to_string("email/password_reset,txt", context)
            html_body = render_to_string("email/password_reset.html", context)

            print(f'link =={link}')
        return user


class PasswordChangeAPIView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = api_serializer.UserSerializer

    def create(self, request, *args, **kwargs):
        payload = request.data
        otp = payload['otp']
        uuid64 = payload['uuid64']
        password = payload['password']

        user = User.objects.get(id=uuid64, otp=otp)
        if user:
            user.set_password(password)
            user.otp = ""
            user.save()
            return Response("Password changed successfully", status=status.HTTP_201_CREATED)
        else:
            return Response("user does not exist", status=status.HTTP_404_NOT_FOUND)
