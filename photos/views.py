import datetime
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Photos, Tags
from .forms import Uploaded


def all_photos(request):
    """ A view to return the photos page"""

    photos = list(Photos.objects.all())
    tags = Tags
    for index, photo in enumerate(photos):
        tag = {
            'tags': photo.tags_set.all()
        }
    print(tags)

    context = {
        'photos': photos,
        'tags': tags,
    }

    if request.method == 'POST':
        timebefore = datetime.datetime.now()
        images = request.FILES.getlist('uploaded-file')
        alltags = request.POST.get('all-tags').split('@')
        for image in images:
            tosave = Photos(
                owner="none",
                upload_date=datetime.datetime.now(),
                image=image,
            )
            tosave.save()
        for tag in alltags:
            if tag != "":
                if Tags.objects.filter(tag_name=tag):
                    savetag = Tags.objects.get(tag_name=tag)
                    savetag.tag_photos.add(tosave)
                else:
                    savetag = Tags(tag_name=tag)
                    savetag.save()
                    savetag.tag_photos.add(tosave)
        return render(request, 'photos/all_photos.html', context)
    else:
        return render(request, 'photos/all_photos.html', context)


def albums(request):
    """ A view to return the albums page"""

    photos = list(Photos.objects.all())
    tags = list(Tags.objects.all())

    context = {
        'photos': photos,
        'tags': tags,
    }

    return render(request, 'photos/albums.html', context)


def tag_album(request, album):
    """ A view to return the photos page"""

    photos = list(Photos.objects.all())
    tags = list(Tags.objects.filter(tag_name=album))

    context = {
        'photos': photos,
        'tags': tags,
    }

    return render(request, 'photos/tag_album.html', context)
