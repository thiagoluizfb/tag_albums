from django.test import TestCase
from .forms import SnackForm


class TestSnackForm(TestCase):

    def test_create_snack_order(self):
        form = SnackForm({
            'f_name': 'Name',
            'l_name': '',
            'email': 'test@gmail.com',
            'street_address1': '123 Street Test',
            'street_address2': '',
            'town_or_city': 'City Test',
            'county': '',
            'country': 'IE',
            'post_code': '',
            'snack_qty': 10,
            'total': 50
            })
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = SnackForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['f_name'][0], 'This field is required.')
