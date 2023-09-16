from django.urls import path
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    
    path('login/', views.login_user, name ='login'),
    path('logout/', views.logout_user, name ='logout'),

     
]
