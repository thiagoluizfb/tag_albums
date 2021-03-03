from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_preview, name='upload_preview'),
<<<<<<< HEAD
    path('photos/', views.all_photos_preview, name='all_photos_preview'),
=======
>>>>>>> ee8cdd25b9a492e0ce02d47662e3a88e8d70ec8b
]
