from django.urls import path
from .views import User

urlpatterns = [
    path('user/<int:pk>/', User.as_view())


]