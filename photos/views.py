from django import forms
from django.shortcuts import render
from .models import Photos, Tags


def upload(request):
    """ A view to return the upload page"""

    return render(request, "upload.html")


def uploaded(request):
    """ A view to update model return the albums page"""

    uploaded = request.POST.get('uploaded')
    files = request.FILES.get('image')

    print(files)
    print("uploaded")

    photos = list(Photos.objects.all())
    tags = list(Tags.objects.all())

    context = {
        'photos': photos,
        'tags': tags,
    }

    return render(request, "albums.html")


def photos(request, album):
    """ A view to return the photos page"""

    photos = list(Photos.objects.all())
    tags = list(Tags.objects.filter(tag_name=album))

    context = {
        'photos': photos,
        'tags': tags,
    }

    return render(request, "photos.html", context)


def albums(request):
    """ A view to return the albums page"""

    photos = list(Photos.objects.all())
    tags = list(Tags.objects.all())

    context = {
        'photos': photos,
        'tags': tags,
    }

    return render(request, "albums.html", context)
