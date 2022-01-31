from django import forms
from django.forms import ModelForm

from .models import Age, BaseAnketa, Menarche, PeriodsAnketa, PeriodsType

YES_OR_NO = ((True, "Да"), (False, "Нет"))


class AnketaForm(ModelForm):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Фамилия Имя Отчество"}
        ),
        label="ФИО:",
    )
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Страна"}
        ),
        label="Страна",
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Город"}),
        label="Город",
    )
    age = forms.CharField(
        widget=forms.RadioSelect(choices=Age.choices,), label="Возраст",
    )
    height = forms.IntegerField(
        min_value=30,
        max_value=250,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Рост"}
        ),
        label="Рост (см)",
    )
    weight = forms.IntegerField(
        min_value=3,
        max_value=350,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Вес"}),
        label="Вес (кг)",
    )

    class Meta:
        model = BaseAnketa
        fields = "__all__"


class PeriodsForm(ModelForm):
    # file = forms.FileField(
    #     widget=forms.FileInput(attrs={"class": "form-control",}),
    #     label="Файл",
    #     required=False,
    # )
    # long_text = forms.CharField(
    #     widget=forms.Textarea(attrs={"class": "form-control",}), label="Длинный текст"
    # )
    menarche = forms.CharField(
        widget=forms.RadioSelect(choices=Menarche.choices,),
        label="С menarche до постановки диагноза",
    )
    periods_type = forms.CharField(
        widget=forms.RadioSelect(choices=PeriodsType.choices,), label="Тип",
    )
    year_break = forms.IntegerField(
        max_value=2022,
        min_value=1900,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "2020"}
        ),
        label="Год нарушения менструального цикла",
    )
    periods_break_variant = forms.CharField(
        widget=forms.RadioSelect(choices=Menarche.choices,),
        label="Вариант нарушения менструального цикла",
    )
    break_type = forms.CharField(
        widget=forms.RadioSelect(choices=PeriodsType.choices,), label="Тип",
    )
    blood = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=YES_OR_NO,
        widget=forms.RadioSelect(),
        label="Маточные кровотечения в анамнезе",
    )
    blood_year = forms.IntegerField(
        max_value=2022, min_value=1900, label="Год", required=False, disabled=True,
    )

    class Meta:
        model = PeriodsAnketa
        fields = "__all__"
