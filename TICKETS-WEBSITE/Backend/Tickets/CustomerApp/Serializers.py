from rest_framework import serializers
import random
from django.contrib.auth.models import User
from .models import otpModel

class sendOtpSerializer(serializers.Serializer):
    phoneNumber = serializers.CharField(max_length=15)
    def create(self, validated_data):
        phone = validated_data.get('PhoneNumber')
        otp=str(random.randint(1000,9999))

        otp_obj,_=otpModel.objects.update_or_create(

            PhoneNumber=phone,
            defaults={'otp': otp, 'is_verified': False}

        )
        print(f"OTP for {phone}: {otp}")  
        return otp_obj
    



class VerifyOtpSerializer(serializers.Serializer):

    phoneNumber = serializers.CharField(max_length=15)
    otp = serializers.CharField()

    def validate(self, data):
        try:
            otp_obj = otpModel.objects.get(phoneNumber=data['phoneNumber'], otp=data['otp'])
        except otpModel.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP or mobile number")

        if otp_obj.is_expired():
            raise serializers.ValidationError("OTP expired")

        otp_obj.is_verified = True
        otp_obj.save()
        return data


class RegisterUserSerializer(serializers.ModelSerializer):
    phoneNumber = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    dob = serializers.DateField()
    address = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['id', 'phoneNumber', 'email', 'address', 'dob', 'password']

    def validate(self, value):
        try:
            otp_obj = otpModel.objects.get(phoneNumber=value)
        except otpModel.DoesNotExist:
            raise serializers.ValidationError("Mobile number not verified")

        if not otp_obj.is_verified:
            raise serializers.ValidationError("Please verify your mobile number first")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


         # Implement your validation logic here
     
         