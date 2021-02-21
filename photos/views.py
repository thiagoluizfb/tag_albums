import datetime
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Photos, Tags
from .forms import Uploaded


def all_photos(request):
    """ A view to return the photos page"""

    photos = list(Photos.objects.all())
    tags = Tags
    context = {
        'photos': photos,
        'tags': tags,
    }

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


def edit_tags(request, image_id):
    """ A view to edit photos tags page"""

    photos = list(Photos.objects.filter(id=image_id))
    tags = Tags
    context = {
        'photos': photos,
        'tags': tags,
        'image_id': image_id,
    }

    if request.method == 'POST':

        tags = request.POST.get('edit-file-tag').split('@')
        tosave = Photos.objects.get(id=image_id)
        tosave.tags_set.clear()
        for tag in tags:
            if tag != "":
                if Tags.objects.filter(tag_name=tag):
                    savetag = Tags.objects.get(tag_name=tag)
                    savetag.tag_photos.add(tosave)
                else:
                    savetag = Tags(tag_name=tag)
                    savetag.save()
                    savetag.tag_photos.add(tosave)

        tags = list(Tags.objects.all())
        for tag in tags:
            if not tag.tag_photos.all():
                todelete = Tags.objects.filter(tag_name=tag)
                todelete.delete()

        return redirect(reverse('all_photos'))

    else:
        return render(request, 'photos/edit_photos.html', context)


def upload(request):
    """ A view to return the upload page"""

    if request.method == 'POST':

        images = request.FILES.get('upload-photo')
        alltags = request.POST.get('edit-file-tag').split('@')
        tosave = Photos(
            owner="none",
            upload_date=datetime.datetime.now(),
            image=images,
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

        redirect(reverse('all_photos'))

    return render(request, "photos/upload.html")
