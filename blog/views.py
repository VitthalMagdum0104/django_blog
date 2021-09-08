from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .models import Blog
from django.contrib import messages
from django. views. decorators. csrf import csrf_exempt

# Create your views here.


def bloghome(request):
    blog = Blog.objects.all()
    context = {'blogs': blog}
    return render(request, 'blog/bloghome.html', context)


def blogpost(request, slug):
    if request.method == 'GET':
        blog = Blog.objects.filter(slug=slug).first()
        context = {'blog': blog}
        return render(request, 'blog/blogpost.html', context)

    if request.method == 'POST':
        blog = Blog.objects.get(slug=slug)
        blog.delete()
        messages.error(request, "Successfully Deleted.")
        return redirect('profile')


def delete(request, serial_no):
    print(serial_no)
    blog = Blog.objects.get(serial_no=serial_no)
    print(blog)
    blog.delete()
    messages.error(request, "Successfully Deleted.")
    return redirect('blog/profile.html')


def create(request):
    return render(request, 'blog/create.html')


def edit(request):
    return render(request, 'blog/create.html')
