from django import forms
from django_recaptcha.fields import ReCaptchaField


class LoginCaptcha(forms.Form):
    captcha = ReCaptchaField()