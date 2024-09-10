from django.shortcuts import render
from .models import Post

zzz=Post.objects.all()

def home(request):
    return render(request,'home.html',{'xxx':zzz})


def about(request):
    return render(request,'about.html')
