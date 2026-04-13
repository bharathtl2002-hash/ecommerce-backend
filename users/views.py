from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from users.serializers import RegisterSerializer
# Create your views here.
class Register(APIView):
	def post(self,request):
		serializer=RegisterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)
class Login(APIView):
	def post(self,request):
		username=request.data.get('username')
		password=request.data.get('password')
		user=authenticate(username=username,password=password)
		if user:
			return Response({
				"message":"Login Success",
				"username":user.username
				})
		return Response({
			"error":"Invalid Credentials"
		},status=status.HTTP_400_BAD_REQUEST)