from django.shortcuts import render


def index(request):
    """ A view to return the index page"""

    return render(request, "home/index.html")


def upload(request):
    """ A view to return the upload page"""

    return render(request, "upload.html")
