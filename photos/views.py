from django.shortcuts import render
from django.contrib import messages
from .models import Photos, Tags
from .forms import Uploaded


def upload(request):
    """ A view to return the upload page"""
    messages.success(request, 'Successfully updated product!')
    return render(request, "upload.html")


def uploaded(request):
    """ A view to update model return the albums page"""

    if request.method == 'POST':
        tosave = Photos(
            owner="none",
            upload_date="today",
            image=request.FILES.get('uploaded-file')
        )
        tosave.save()
    else:
        photos = Uploaded()

    photos = list(Photos.objects.all())
    tags = list(Tags.objects.all())

    context = {
        'photos': photos,
        'tags': tags,
    }

    return render(request, "albums.html", context)


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
