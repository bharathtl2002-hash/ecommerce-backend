from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from orders.models import Order
from orders.serializers import OrderSerializer
# Create your views here.
class OrderList(APIView):
	def get(self,request):
		o=Order.objects.all()
		o1=OrderSerializer(o,many=True,context={'request':request})
		return Response(o1.data)
	def post(self,request):
		o1=OrderSerializer(data=request.data,context={'request':request})
		if o1.is_valid():
			o1.save()
			return Response(o1.data)
		return Response(o1.errors)
class OrderDetails(APIView):
	def get(self,request,id):
		try:
			o=Order.objects.get(id=id)
		except Order.DoesNotExist:
			return Response(status=404)
		o1=OrderSerializer(o,context={'request':request})
		return Response(o1.data)
	def put(self,request,id):
		try:
			o=Order.objects.get(id=id)
		except Order.DoesNotExist:
			return Response(status=404)
		o1=OrderSerializer(o,data=request.data,context={'request':request})
		if o1.is_valid():
			o1.save()
			return Response(o1.data)
		return Response(o1.errors,status=status.HTTP_400_BAD_REQUEST)
	def delete(self,request,id):
		try:
			o=Order.objects.get(id=id)
		except Order.DoesNotExist:
			return Response(status=404)
		o.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)