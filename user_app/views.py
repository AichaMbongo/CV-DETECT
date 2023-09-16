from django.shortcuts import render, get_object_or_404, redirect
from .models import User
# from .forms import UserForm  # Create a form for user input
from django_otp.plugins.otp_totp.models import TOTPDevice
# from django_otp.plugins.otp_totp.util import verify_token


from django.contrib.auth.decorators import login_required
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth import logout
from django.contrib.auth import authentication, login
from django.shortcuts import render, redirect
from .forms import UserLoginForm  # Import your login form


from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


from django.contrib import messages





from django.contrib import messages



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username, password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success

            return render(request, "login.html", {})

def logout_user(request):
    pass

