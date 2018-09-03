from django.shortcuts import render

from .models import Blog


def index(req):

    blogs = Blog.objects.all()
    return render(req, 'blog/index.html', {'blogs': blogs})
