from django.urls import path, include
from .views import Home, Form,checkformUser

urlpatterns = [
    path('', Home, name='home'),
    path('checkform/', Form, name='checkform'),
    path('checkformuser', checkformUser, name='checkformUser'),
]
