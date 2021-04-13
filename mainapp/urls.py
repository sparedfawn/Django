from django.urls import path
from .views import DetailedView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('<int:pk>/', DetailedView.as_view(), name='base'),
]
