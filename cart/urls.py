from django.urls import path
from cart.views import CartList,CartDetails
urlpatterns=[
			
			path('',CartList.as_view()),
			path('<int:id>/',CartDetails.as_view())
]