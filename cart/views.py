from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from cart.models import Cart
from cart.serializers import CartSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class CartList(APIView):
	permission_classes=[IsAuthenticated]
	def get(self,request):
		c=Cart.objects.filter(user=request.user)
		c1=CartSerializer(c,many=True,context={'request':request})
		return Response(c1.data)
	def post(self,request):
		data=request.data.copy()
		data['user']=request.user.id
		c1=CartSerializer(data=data,context={'request':request})
		if c1.is_valid():
			c1.save()
			return Response(c1.data)
		return Response(c1.errors)
class CartDetails(APIView):
	permission_classes=[IsAuthenticated]
	def get(self,request,id):
		try:
			c=Cart.objects.get(id=id,user=request.user)
		except Cart.DoesNotExist:
			return Response(status=404)
		c1=CartSerializer(c,context={'request':request})
		return Response(c1.data)
	def put(self,request,id):
		try:
			c=Cart.objects.get(id=id,user=request.user)
		except Cart.DoesNotExist:
			return Response(status=404)
		c1=CartSerializer(c,data=request.data,context={'request':request})
		if c1.is_valid():
			c1.save()
			return Response(c1.data)
		return Response(c1.errors,status=status.HTTP_400_BAD_REQUEST)
	def delete(self,request,id):
		try:
			c=Cart.objects.get(id=id,user=request.user)
		except Cart.DoesNotExist:
			return Response(status=404)
		c.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


