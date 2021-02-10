from django.shortcuts import render
from .models import Photos, Tags


def upload(request):
    """ A view to return the upload page"""

    return render(request, "upload.html")


def uploaded_photos(request):
    """ A view to return the photos page"""

    uploaded_photos = Photos.objects.all()
    tags = Tags.objects.all()


    context = {
        'uploaded_photos': uploaded_photos,
        'tags': tags,
    }

    return render(request, "uploaded_photos.html", context)
