from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/', views.DetailedView.as_view(), name='base'),
    path('register', views.register, name='register'),
]
