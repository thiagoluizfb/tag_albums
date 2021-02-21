from django.utils import timezone
from django.test import TestCase
from .models import Photos, Tags


class TestViews(TestCase):

    def test_all_photos(self):
        response = self.client.get('/photos/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/all_photos.html')

    def test_upload(self):
        response = self.client.get('/photos/upload')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/upload.html')

    def test_delete_img(self):
        creationDate = timezone.now()
        photo = Photos.objects.create(owner="none", upload_date=f'{creationDate}')
        response = self.client.get(f'/photos/delete/{photo.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/delete_photos.html')

    def test_edit_tags(self):
        creationDate = timezone.now()
        photo = Photos.objects.create(owner="none", upload_date=f'{creationDate}')
        response = self.client.get(f'/photos/edit/{photo.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/edit_photos.html')

    def test_tag_album(self):
        tag = Tags.objects.create(tag_name="summer")
        response = self.client.get(f'/photos/albums/{tag.tag_name}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/tag_album.html')

    def test_albums(self):
        response = self.client.get('/photos/albums/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/albums.html')
