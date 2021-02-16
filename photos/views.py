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
        images = request.FILES.getlist('uploaded-file')
        tags = request.POST.get('each-tag').split(',')
        for count, image in enumerate(images):
            if not Photos.objects.filter(image=image):
                tosave = Photos(
                    owner="none",
                    upload_date="today",
                    image=image,
                )
                tosave.save()
            else:
                tosave = Photos.objects.get(image=image)
            eachtag = tags[count].split('@')
            for tag in eachtag:
                if tag != "":
                    if Tags.objects.filter(tag_name=tag):
                        savetag = Tags.objects.get(tag_name=tag)
                        savetag.tag_photos.add(tosave)
                    else:
                        savetag = Tags(tag_name=tag)
                        savetag.save()
                        savetag.tag_photos.add(tosave)
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
