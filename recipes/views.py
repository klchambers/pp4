from django.shortcuts import render # noqa
from django.http import HttpResponse


# Create your views here.
def my_site(request):
    return HttpResponse('Hello, world!')
