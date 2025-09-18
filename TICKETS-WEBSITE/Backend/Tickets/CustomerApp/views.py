from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializers import *

class SendOTPView(APIView):
    def post(self, request):
        serializer = sendOtpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "OTP generated and sent (simulated)."})
        return Response(serializer.errors, status=400)


class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "OTP verified successfully."})
        return Response(serializer.errors, status=400)


class RegisterUserView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=201)
        return Response(serializer.errors, status=400)
