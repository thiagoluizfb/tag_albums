import datetime
from django.shortcuts import render, redirect, reverse
from photos.views import Photos, Tags


def index(request):
    """ A view to return the index page"""

    return render(request, "home/index.html")


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

        return redirect(reverse('all_photos'))

    return redirect(reverse('all_photos'))
