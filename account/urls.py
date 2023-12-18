from django.urls import path
from .views import *

urlpatterns = [
    path('register/',UserRegistration.as_view())  # .as_view() - джанго понимает класса в качестве view
]