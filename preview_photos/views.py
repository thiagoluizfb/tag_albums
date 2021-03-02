from django.shortcuts import render, redirect, reverse


def upload_preview(request):
    """ A view to return the upload page"""

    if request.method == 'POST':

        images = request.FILES.get('upload-photo')
        alltags = request.POST.get('edit-file-tag').split('@')

        preview = request.session.get('preview', {})
        src = request.POST.get('img-src')
        preview[images.name] = {
            'src': src,
            'tags': alltags,
        }
        request.session['preview'] = preview
        # return redirect(reverse('all_photos_preview'))

    return render(request, "preview_photos/upload_preview.html")
