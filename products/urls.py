from django.urls import path
from products.views import ProductList,ProductDetails

urlpatterns=[
		
		path('',ProductList.as_view()),
		path('<int:id>/',ProductDetails.as_view())
]