from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_photos, name='all_photos'),
    path('upload', views.upload, name='upload'),
    path('edit/<int:image_id>/', views.edit_tags, name='edit_tags'),
    path('delete/<int:image_id>/', views.delete_img, name='delete_img'),
    path('albums/', views.albums, name='albums'),
    path('albums/<album>/', views.tag_album, name='tag_album')
]
