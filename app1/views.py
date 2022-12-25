from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sekhar(request):
    return HttpResponse('<marquee><h1>sekhar is my roommate</h1></marquee>')
