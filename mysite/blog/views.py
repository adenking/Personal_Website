from django.shortcuts import render
from django.views import generic


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'blog/about.html')