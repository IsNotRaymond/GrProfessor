from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('signup/', views.signupView, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]