from django.utils import timezone
from django.test import TestCase
from .models import Photos, Tags


class TestModels(TestCase):

    def test_model_entries(self):
        creationDate = timezone.now()
        photo = Photos.objects.create(owner="none", upload_date=f'{creationDate}')
        self.assertEqual(photo.owner, "none")

    def test_photos_owner_method_returns_owner(self):
        creationDate = timezone.now()
        photo = Photos.objects.create(owner="none", upload_date=f'{creationDate}')
        self.assertEqual(str(photo), "none")

    def test_tags_entries(self):
        tag = Tags.objects.create(tag_name='summer')
        self.assertEqual(tag.tag_name, 'summer')

    def test_tag_tag_name_method_returns_tag_name(self):
        tag = Tags.objects.create(tag_name='summer')
        self.assertEqual(str(tag), "summer")
