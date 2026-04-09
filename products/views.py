from django.shortcuts import render
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
# Create your views here.
class ProductList(APIView):
	def get(self,request):
		category=request.GET.get('category')
		search=request.GET.get('search')
		page=request.GET.get('page',1)
		ordering=request.GET.get('ordering')
		p=Product.objects.all()
		if category:
			p=p.filter(category__name=category)
		if search:
			p=p.filter(name__icontains=search)
		if ordering:
			p=p.order_by(ordering)
		paginator=Paginator(p,60)
		page_obj=paginator.get_page(page)
		p1=ProductSerializer(page_obj.object_list,many=True,context={'request':request})
		return Response(p1.data)
	def post(self,request):
		p1=ProductSerializer(data=request.data)
		if p1.is_valid():
			p1.save()
			return Response(p1.data)
		return Response(p1.errors)
class ProductDetails(APIView):
	def get(self,request,id):
		try:
			p=Product.objects.get(id=id)
		except p.DoesNotExist:
			return Response(status=404)
		p1=ProductSerializer(p,context={'request':request})
		return Response(p1.data)
	def put(self,request,id):
		try:
			p=Product.objects.get(id=id)
		except p.DoesNotExist:
			return Response(status=404)
		p1=ProductSerializer(p,data=request.data,context={'request':request})
		if p1.is_valid():
			p1.save()
			return Response(p1.data)
		return Response(p1.errors,status=status.HTTP_400_BAD_REQUEST)
	def delete(self,request,id):
		try:
			p=Product.objects.get(id=id)
		except p.DoesNotExist:
			return Response(status=404)
		p.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


