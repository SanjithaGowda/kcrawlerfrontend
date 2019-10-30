from django.forms import ModelForm, Form
from .models import EntryItem
from django import forms
class EntryItemForm(ModelForm):
    keyword = forms.CharField(label='')
    class Meta:
        model = EntryItem
        fields = ("keyword",)