from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # DB queries
    # logic
    # encode results
    return HttpResponse("Hello, world. You're at the polls index.")


def index_t(request):
    # DB queries
    # logic
    # encode results
    return HttpResponse("123s")
