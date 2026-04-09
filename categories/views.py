from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from categories.models import Category
from rest_framework import status
from categories.serializers import CategorySerializer
# Create your views here.
class CategoryList(APIView):
	def get(self,request):
		c=Category.objects.all()
		c1=CategorySerializer(c,many=True)
		return Response(c1.data)
	def post(self,request):
		c1=CategorySerializer(data=request.data)
		if c1.is_valid():
			c1.save()
			return Response(c1.data)
		return Response(c1.errors)
class CategoryDetails(APIView):
	def get(self,request,id):
		try:
			c=Category.objects.get(id=id)
		except c.DoesNotExist:
			return Response(status=404)
		c1=CategorySerializer(c)
		return Response(c1.data)
	def put(self,request,id):
		try:
			c=Category.objects.get(id=id)
		except c.DoesNotExist:
			return Response(status=404)
		c1=CategorySerializer(c,data=request.data)
		if c1.is_valid():
			c1.save()
			return Response(c1.data)
		return Response(c1.errors,status=status.HTTP_400_BAD_REQUEST)
	def delete(self,request,id):
		try:
			c=Category.objects.get(id=id)
		except c.DoesNotExist:
			return Response(status=404)
		c.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)