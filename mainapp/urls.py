from django.urls import path
from .views import Detailed

urlpatterns = [
    path('<int:pk>/', Detailed.as_view(), name='detailed')
]