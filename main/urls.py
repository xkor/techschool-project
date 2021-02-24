from django.urls import path
from .views import CustomerUpdateView, CustomerCreateView


urlpatterns = [
    path('customer/', CustomerCreateView.as_view()),
    path('customer/<int:pk>', CustomerUpdateView.as_view())
]
