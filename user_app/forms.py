from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    otp_token = forms.CharField(
        label="2FA Token",
        max_length=6,  # Adjust the length as needed for your OTP tokens
        required=False,  # OTP is optional during login
    )


# forms.py
from django import forms

class Enable2FAForm(forms.Form):
    method_choices = (
        ('totp', 'Time-Based One-Time Password (TOTP)'),
        ('sms', 'SMS Verification'),
    )

    method = forms.ChoiceField(choices=method_choices, widget=forms.RadioSelect)
