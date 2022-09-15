from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=8, label='Password', widget=forms.PasswordInput(attrs={'placeholder':'parol'}))
    repeat_password = forms.CharField(min_length=8, label='Repeat password', widget=forms.PasswordInput(attrs={'placeholder':'parolni qayta yozing'}))

    class Meta:
        model = User
        fields = ('name', 'surname', 'username', 'age', 'phone', 'gender', 'address')
        widgets = {
            "username":forms.widgets.TextInput(attrs={'class':'input', 'placeholder':'Foydalanuvchi nomi', 'autocomplete':"off"}),
            "name":forms.widgets.TextInput(attrs={'class':'input', 'placeholder':'Ismingiz', 'autocomplete':"off"}),
            "surname":forms.widgets.TextInput(attrs={'class':'input', 'placeholder':'Familyangiz', 'autocomplete':"off"}),
            'age': forms.TextInput(attrs={'class': 'unique d-block', 'placeholder': 'Yoshingiz', 'autocomplete':"off"}),
            'phone': forms.TextInput(attrs={'placeholder': 'Nomeringiz', 'class': '' , 'autocomplete':"off"})
        }



    def clean_repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['repeat_password']



