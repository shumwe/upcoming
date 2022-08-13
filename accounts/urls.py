from django.urls import path
from accounts import views

urlpatterns = [
    path('dashboard/', views.profile, name='profile'),
]