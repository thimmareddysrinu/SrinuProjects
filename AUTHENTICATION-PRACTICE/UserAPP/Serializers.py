from rest_framework import serializers
from .models import OTPVerification
from django.contrib.auth.models import User
import random

class SendOTPSerializer(serializers.Serializer):
    mobile = serializers.CharField()

    def create(self, validated_data):
        mobile = validated_data['mobile']
        otp = str(random.randint(100000, 999999))
        otp_obj, _ = OTPVerification.objects.update_or_create(
            mobile=mobile,
            defaults={'otp': otp, 'is_verified': False}
        )
        # Simulate sending OTP (no external service)
        print(f"SIMULATED: Sending OTP {otp} to {mobile}")
        return otp_obj


class VerifyOTPSerializer(serializers.Serializer):
    mobile = serializers.CharField()
    otp = serializers.CharField()
    def validate(self, data):
        try:
            otp_obj = OTPVerification.objects.get(mobile=data['mobile'], otp=data['otp'])
        except OTPVerification.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP or mobile number")
        if otp_obj.is_expired():
            raise serializers.ValidationError("OTP expired")
        otp_obj.is_verified = True
        otp_obj.save()
        return data


class RegisterUserSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField()

    class Meta:

        model = User

        fields = ['username', 'password', 'mobile']

        extra_kwargs = {'password': {'write_only': True}}

    def validate_mobile(self, value):
        try:
        
            otp_obj = OTPVerification.objects.get(mobile=value)

        except OTPVerification.DoesNotExist:
        
            raise serializers.ValidationError("Mobile number not verified")
        
        if not otp_obj.is_verified:
           
            raise serializers.ValidationError("Please verify your mobile number first")
        
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            PhoneNumber=validated_data['PhoneNumber'],
            password=validated_data['password']
        )
        
        return user
