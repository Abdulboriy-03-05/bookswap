from email.headerregistry import Address
from django import forms
from .models import Book
from account.models import User

class StockSearchForm(forms.ModelForm):
    query = forms.CharField()
    query.widget.attrs.update({'placeholder': 'qidiruv',})
    class Meta:
        model = Book
        fields = ['genre','location']