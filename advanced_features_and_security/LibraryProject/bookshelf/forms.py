from django import True
from .models import Book

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=100)
