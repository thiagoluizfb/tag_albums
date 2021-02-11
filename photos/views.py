from django.shortcuts import render
from .models import Photos, Tags


def upload(request):
    """ A view to return the upload page"""

    return render(request, "upload.html")


def photos(request, album):
    """ A view to return the photos page"""

    photos = list(Photos.objects.all())
    tags = list(Tags.objects.filter(tag_name=album))
    print(tags[0])

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
