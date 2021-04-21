from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/', views.DetailedView.as_view(), name='base'),
    path('<int:pk>/bin/', views.BinView.as_view(), name='bin'),
    path('<int:pk>/favourites/', views.FavouriteView.as_view(), name='favourite'),
    path('register', views.register, name='register'),
    path('<int:user_id>/<int:pk>', views.InDirectoryView.as_view(), name='inDirectory'),
]
