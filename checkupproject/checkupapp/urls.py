from django.urls import path, include
from .views import Home, Form

urlpatterns = [
    path('', Home),
    path('checkform/', Form, name='checkform'),
]
