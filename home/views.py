import datetime
from django.shortcuts import render, redirect, reverse
from photos.views import Photos, Tags


def index(request):
    """ A view to return the index page"""

    return render(request, "home/index.html")


def upload(request):
    """ A view to return the upload page"""

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
    return render(request, "upload.html")


def albums(request):
    """ A view to return the albums page"""

    photos = list(Photos.objects.all())
    tags = list(Tags.objects.all())

    context = {
        'photos': photos,
        'tags': tags,
    }
    return render(request, "albums.html", context)
