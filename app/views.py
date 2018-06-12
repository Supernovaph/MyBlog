from django.http import HttpResponse, HttpResponseBadRequest
from .models import BlogUser, Post

from django.shortcuts import render

def publish(request):
    pass
    # post = Post(title=request.POST['title'], text=..., created=)

def register(request):
    if 'login' in request.POST and 'password' in request.POST:
        user = BlogUser(login=request.POST['login'], password=request.POST['password'])
        user.save()
        return HttpResponse('success!')
    else:
        return render(request, 'register.html')

