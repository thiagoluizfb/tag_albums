from django.shortcuts import render, redirect, reverse
from django.conf import settings
from .models import PhotosPreview

import uuid


def upload_preview(request):
    """ A view to return the upload preview page"""

    if request.method == 'POST':

        images = request.FILES.get('upload-photo')
        alltags = request.POST.get('edit-file-tag').split('@')
        image_id = str(uuid.uuid4())
        todelete = PhotosPreview.objects.all()
        todelete.delete()
        tosave = PhotosPreview(
            image=images,
            image_name=image_id
        )
        tosave.save()

        preview = request.session.get('preview', {})
        photo_id = len(preview)
        preview[photo_id] = {
            'id': photo_id,
            'tags': alltags,
            'image': images.name,
            'image_id': image_id,
        }
        request.session['preview'] = preview
        return redirect(reverse('all_photos_preview'))

    return render(request, "preview_photos/upload_preview.html")


def all_photos_preview(request):
    """ A view to return the photos preview page"""

    location = settings.MEDIA_URL
    preview = request.session.get('preview', {})
    photos = []
    for p in preview:
        photos.append(preview[p])
    context = {
        'photos': photos,
        'location': location,
    }

    return render(request, 'preview_photos/all_photos_preview.html', context)
