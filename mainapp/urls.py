from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('drive/bin/', views.binPage, name='bin'),
    path('drive/favourites/', views.favouritePage, name='favourite'),
    path('sign-up', views.register, name='register'),
    path('drive/<int:pk>', login_required(login_url='login')(views.InDirectoryView.as_view()), name='inDirectory'),
    path('sign-in', views.loginPage, name='login'),
    path('drive', views.drivePage, name='drive'),
    path('logout', views.logoutUser, name='logout')
]
