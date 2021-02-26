from django import forms
from .models import Snack


class SnackForm(forms.ModelForm):
    class Meta:
        model = Snack
        fields = ('f_name', 'l_name', 'email',
                  'street_address1', 'street_address2',
                  'town_or_city', 'county', 'country',
                  'postcode', 'snack_qty', 'total')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'f_name': 'Full Name',
            'l_name': 'Last Name',
            'email': 'Email Address',
            'street_address1': 'Street address',
            'street_address2': 'Street address',
            'town_or_city': 'Town or City',
            'county': 'County',
            'country': 'Country',
            'postcode': 'Post Code',
            'snack_qty': '1',
            'total': 'total',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
