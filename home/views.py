import datetime
from django.shortcuts import render, redirect, reverse
from photos.views import Photos, Tags


def index(request):
    """ A view to return the index page"""

    return render(request, "home/index.html")


def upload(request):
    """ A view to return the upload page"""

    return render(request, "home/upload.html")
