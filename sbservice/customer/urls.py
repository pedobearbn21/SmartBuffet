"""sbservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from customer.views import OrderView, OrderIDView, MeatView, MeatIDView,Search,GraphTotalCustomer, OrderPost
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'meat', OrderPost, basename='user')
# urlpatterns = router.urls
urlpatterns = [
    path('orderlist', OrderView.as_view()),
    path('order/<int:id>', OrderIDView.as_view()),
    
    path('meatlist', MeatView.as_view()),
    path('meat/<int:id>', MeatIDView.as_view()),
    path('meat/search/<int:type>', Search.as_view()),
    #Graph Total Customer Today
    path('totalcustomer', GraphTotalCustomer.as_view())
]
