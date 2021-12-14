from django.forms import ModelForm
from .models import Anketa, Colors
from django import forms


class AnketaForm(ModelForm):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Фамилия Имя Отчество'}),
        label='ФИО:'
    )
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Город'}),
        label='Город'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                'placeholder': 'mail@example.com'}),
        label='Email'
    )
    age = forms.IntegerField(
        max_value=100,
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                'placeholder': '25'}),
        label='Возраст'
    )
    color = forms.CharField(
        widget=forms.Select(
            choices=Colors.choices,
            attrs={
                "class": "form-control",
            }),
        label='Цвет'
    )
    file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
            }),
        label='Файл',
        required=False
    )
    long_text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
            }),
        label='Длинный текст'
    )

    class Meta:
        model = Anketa
        fields = ('full_name',
                  'city',
                  'email',
                  'age',
                  'color',
                  'file',
                  'long_text')
