from django.urls import path
from categories.views import CategoryList,CategoryDetails

urlpatterns=[

			path('',CategoryList.as_view()),
			path('<int:id>/',CategoryDetails.as_view())
]