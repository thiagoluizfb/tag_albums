from django.shortcuts import render, redirect, reverse
from django.conf import settings
from .models import PhotosPreview

import uuid


def upload_preview(request):
    """ A view to return the upload preview page"""

    if request.method == 'POST':

        images = request.FILES.get('upload-photo')
        alltags = request.POST.get('edit-file-tag').split('@')
        tags = []
        for tag in alltags:
            if tag != "":
                tags.append(tag)

        image_id = str(uuid.uuid4())
        tosave = PhotosPreview(
            image=images,
            image_name=image_id
        )
        tosave.save()

        preview = request.session.get('preview', {})
        photo_id = len(preview)
        preview[photo_id] = {
            'id': photo_id,
            'tags': tags,
            'image': tosave.image.name,
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


def albums_preview(request):
    """ A view to return the albums preview page"""

    location = settings.MEDIA_URL
    preview = request.session.get('preview', {})
    photos = []
    for p in preview:
        photos.append(preview[p])

    alltags = []
    for tags in photos:
        for tag in tags['tags']:
            alltags.append(tag)
    tags = list(set(alltags))
    tag_albums = {}
    for tag in tags:
        tag_id = len(tag_albums)
        images = []
        for photo in photos:
            if tag in photo['tags']:
                images.append(photo['image'])
            tag_albums[tag_id] = {
                'tag': tag,
                'images': images,
            }
    albums = []
    for tag in tag_albums:
        albums.append(tag_albums[tag])

    request.session['albums'] = albums

    context = {
        'albums': albums,
        'location': location,
    }

    return render(request, 'preview_photos/albums_preview.html', context)


def edit_tags_preview(request, image_id):
    """ A view to edit photos' tags page"""

    location = settings.MEDIA_URL
    preview = request.session.get('preview', {})
    photo = preview[f'{image_id}']
    tags = photo['tags']

    template = 'preview_photos/edit_photos_preview.html'
    context = {
        'photo': photo,
        'tags': tags,
        'location': location,
    }

    if request.method == 'POST':

        newtags = request.POST.get('edit-file-tag').split('@')
        tags = []
        for tag in newtags:
            if tag != "":
                tags.append(tag)
        preview[f'{image_id}']['tags'] = tags
        request.session['preview'] = preview

        return redirect(reverse('all_photos_preview'))

    else:
        return render(request, template, context)


def tag_album_preview(request, album):
    """ A view to return the tag album page"""

    location = settings.MEDIA_URL
    albums = request.session.get('albums', {})
    for tag_album in albums:
        if tag_album['tag'] == album:
            album = tag_album

    context = {
        'album': album,
        'location': location,
    }

    return render(request, 'preview_photos/tag_album_preview.html', context)
