from django.shortcuts import render
from photos.views import Photos, Tags
from photos.forms import Uploaded


def index(request):
    """ A view to return the index page"""

    return render(request, "home/index.html")


def upload(request):
    """ A view to return the upload page"""

    photos = list(Photos.objects.all())
    tags = list(Tags.objects.all())
    context = {
        'photos': photos,
        'tags': tags
    }
    return render(request, "upload.html", context)
