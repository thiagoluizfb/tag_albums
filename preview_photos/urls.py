from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_preview, name='upload_preview'),
    path('photos/', views.all_photos_preview, name='all_photos_preview'),
    path('albums/', views.albums_preview, name='albums_preview'),
    path('edit/<int:image_id>/', views.edit_tags_preview, name='edit_tags_preview'),
    path('albums/<album>/', views.tag_album_preview, name='tag_album_preview'),
]
