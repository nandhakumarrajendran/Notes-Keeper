from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from User_Auth.forms import LoginCaptcha
from .models import ContactUs

#Import Packages For Email Sending
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')

        if password != c_password:
            messages.error(request, 'Password Does Not Match!')
            return redirect('signup')

        try:
            if User.objects.get(username=uname):
                messages.info(request, 'Username is Already Exist!')
                return redirect('signup')
        except:
            pass

        try:
            if User.objects.get(email=email):
                messages.info(request, 'Email is Already Exist!')
                return redirect('signup')
        except:
            pass

        myuser = User.objects.create_user(
            username=uname, first_name=fname, last_name=lname, email=email, password=password)
        myuser.save()
        messages.success(request, 'Thank you for Signin!')
        return redirect('login')

    return render(request, 'signup.html')


def loginpage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        form = LoginCaptcha(request.POST)
        
        myuser = authenticate(username=uname, password=password)
        if myuser is not None:
            
            if not form.is_valid():
                messages.error(request, 'Please check reCAPTCHA')
                return redirect('login')
            
            else:
                login(request, myuser)
                messages.success(request, f'Welcome {uname}!')
                return redirect('home')
        
        else:
            messages.error(request, 'Invalid Username and Password!')
            return redirect('login')
    

    else:
        form = LoginCaptcha()
        
    context = {'form': form}
    return render(request, 'login.html', context)


def logoutpage(request):
    logout(request)
    messages.warning(request, 'Thanks For Visiting Our Page!')
    return redirect('login')

def contact(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Content = request.POST.get('content')
        
        Data = ContactUs(Name = Name, Email = Email, Phone = Phone, Content = Content)
        Data.save()
        
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        
        email_message = mail.EmailMessage(f'Email From {Name}', f'User Email: {Email}\nUser Phone Number: {Phone}\n\n\n QEARY : {Content}',from_email,['nandhakumarrajendran15@gmail.com'], connection= connection)
        
        email_client = mail.EmailMessage('Notes Keeper Response','Thanks For Reaching us \n\n We will get back You Soon My Friend \n\n Contact Us nandhakumarrajendran15@gmail.com',from_email,[Email],connection=connection)

        connection.send_messages([email_message,email_client])
        connection.close()
        
        messages.info(request, "Thanks For Reaching Us! We will get back you soon...")
        return redirect('contact')
    
    
    return render(request, 'contact.html')


def help(request):
    return render(request, 'help.html')

