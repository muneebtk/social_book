from django import forms
from . models import Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        # fields = ['title', 'author', 'description',
        #           'price', 'file', 'visibility', 'book']
        fields = '__all__'
