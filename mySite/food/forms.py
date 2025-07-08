from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["Item_name", "Item_descr", "unit_price", "Item_image"]