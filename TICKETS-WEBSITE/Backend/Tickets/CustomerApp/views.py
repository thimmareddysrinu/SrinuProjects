from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializers import *
from rest_framework import status

# class SendOTPView(APIView):
#     def post(self, request):
#         serializer = sendOtpSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "OTP generated and sent (simulated)."})
#         return Response(serializer.errors, status=400)


# class VerifyOTPView(APIView):
#     def post(self, request):
#         serializer = VerifyOtpSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response({"message": "OTP verified successfully."})
#         return Response(serializer.errors, status=400)


# class RegisterUserView(APIView):
#     def post(self, request):
#         serializer = RegisterUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User registered successfully."}, status=201)
#         return Response(serializer.errors, status=400)

#    ########### write coding for ticketing #############



class MovieNameView(APIView):
    def get(self, request):
        movies = MovieName.objects.all()
        serializer = MovieNameSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieNameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieNameView(APIView):
    def get(self,request):
       moviesname=MovieName.objects.all()
       serializers =MovieNameSerializer(moviesname,many=True)
       return Response(serializers.data)
      
    def post(self, request):
        serializer = MovieNameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieTicketingView(APIView):
    queryset=MovieName.objects.all()
    serializers =MovieTicketingSerializer
class ShowTimeView(APIView):
    queryset=Showtime.objects.all()
    serializers =ShowTimeSerializer
class TheatreNameView(APIView):
    queryset=TheaterName.objects.all()
    serializers =TheartreSerializer
class SeatView(APIView):
    queryset=Seat.objects.all()
    serializers =SeatSerializer
