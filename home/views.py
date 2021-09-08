from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Blog
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


def home(request):
    blog = Blog.objects.all()
    try:
        context = {'blog': blog[0:3]}
        return render(request, 'home/home.html', context)
    except:
        return render(request, 'home/home.html')


def about(request):
    return render(request, "home/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 9 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(
                request, "Your message has been successfully sent")
    return render(request, "home/contact.html")


def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10 or not username.isalnum():
            messages.error(
                request, " Username must contain letters,numbers and less than 10 chars.")
            return redirect('home')

        if pass1 != pass2:
            messages.error(
                request, " Passwords should match.")
            return redirect('home')

        # Create the user
        user = User.objects.create_user(username, email, pass1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.success(
            request, " Your blogger account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, " Successfully Logged In.")
            return redirect('home')

        else:
            messages.error(
                request, " Invalid credintials, Please try again.")
            return redirect('home')


def user_logout(request):
    logout(request)
    messages.error(request, "Successfully Logout.")
    return redirect('home')


def profile(request):
    blogs = Blog.objects.filter(author=request.user.id)
    context = {'blogs': blogs}
    return render(request, 'blog/profile.html', context)
