from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    text_ = "Hello world !\nThe test website for IBM portal 1."
    return HttpResponse(text_)

def portal_test(request):
    return render(request, "PortalTest.html")

def demo(request):
    return render(request, "demo.html")