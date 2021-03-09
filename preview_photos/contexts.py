def preview(request):

    photos = []
    preview = request.session.get('preview', {})

    context = {
        'photos': photos,
    }

    return context
