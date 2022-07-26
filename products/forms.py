from django import forms
from models import Product


class ProductForm(forms.ModelsForm):
    class meta:
        model = Product
        Fields = [
            'Titile',
            'Content',
            'Price'
        ]
