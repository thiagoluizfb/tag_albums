from django.shortcuts import render, redirect, reverse
<<<<<<< HEAD
from django.conf import settings


def upload_preview(request):
    """ A view to return the upload preview page"""
=======


def upload_preview(request):
    """ A view to return the upload page"""
>>>>>>> ee8cdd25b9a492e0ce02d47662e3a88e8d70ec8b

    if request.method == 'POST':

        images = request.FILES.get('upload-photo')
        alltags = request.POST.get('edit-file-tag').split('@')

        preview = request.session.get('preview', {})
        src = request.POST.get('img-src')
<<<<<<< HEAD
        photo_id = len(preview)
        preview[photo_id] = {
            'id': photo_id,
=======
        preview[images.name] = {
>>>>>>> ee8cdd25b9a492e0ce02d47662e3a88e8d70ec8b
            'src': src,
            'tags': alltags,
        }
        request.session['preview'] = preview
<<<<<<< HEAD
        return redirect(reverse('all_photos_preview'))

    return render(request, "preview_photos/upload_preview.html")


def all_photos_preview(request):
    """ A view to return the photos preview page"""

    location = settings.MEDIA_URL
    preview = request.session.get('preview', {})
    photos = []
    for p in preview:
        photos.append(preview[p])
        print(photos)
    context = {
        'photos': photos,
        'location': location,
    }

    return render(request, 'preview_photos/all_photos_preview.html', context)
=======
        # return redirect(reverse('all_photos_preview'))

    return render(request, "preview_photos/upload_preview.html")
>>>>>>> ee8cdd25b9a492e0ce02d47662e3a88e8d70ec8b
