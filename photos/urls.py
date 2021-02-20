from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_photos, name='all_photos'),
    path('edit/<int:image_id>/', views.edit_tags, name='edit_tags'),
    path('albums/', views.albums, name='albums'),
    path('albums/<album>/', views.tag_album, name='tag_album'),
    path('upload', views.upload, name='upload')
]
