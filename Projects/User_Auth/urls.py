from django.urls import path
from User_Auth import views



urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginpage, name='login'),
    path('signup', views.signuppage, name='signup'),
    path('logout', views.logoutpage, name="logout"),
    path('contact', views.contact, name="contact"),
    path('help', views.help, name="help"),

    
]
