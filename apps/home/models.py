# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models


class Age(models.TextChoices):
    a20_25 = "age_20_25", "20-25"
    a26_30 = "age_26_30", "26-30"
    a31_35 = "age_31_35", "31-35"
    a36_40 = "age_36_40", "36-40"
    a41_45 = "age_41_45", "41-45"
    a46_50 = "age_46_50", "46-50"


class Colors(models.TextChoices):
    WHITE = "WHITE", "Белый"
    PINK = "PINK", "Розовый"
    GREEN = "GREEN", "Зеленый"
    YELLOW = "YELLOW", "Желтый"
    RED = "RED", "Красный"


class Menarche(models.TextChoices):
    CH1 = "24-38/3-8", "24-38/3-8"
    CH2 = "24-38/>8", "24-38/>8"
    CH3 = "23 и </3-8", "23 и </3-8"
    CH4 = "23 и </>8", "23 и </>8"
    other = "другое", "другое"


class PeriodsType(models.TextChoices):
    BIG = "Обильные", "Обильные"
    NORMAL = "нормальные", "нормальные"
    SMALL = "судные", "судные"


class Contraception(models.TextChoices):
    PPA = "прерванный половой акт", "прерванный половой акт"
    gondon = "изделие №2", "изделие №2"
    con3 = "спермициды", "спермициды"
    kgk = "КГК", "КГК"
    progestin = "чистые прогестины", "чистые прогестины"
    vmk = "ВМК", "ВМК"
    mirena = "рилизинг система Мирена", "рилизинг система Мирена"
    ring = "Нова-ринг", "Нова-ринг"
    transdermal = "Трансдермальная система", "Трансдермальная система"


class MammaryDiseases(models.TextChoices):
    benign = "доброкачественные", "доброкачественные"
    border = "пограничные", "пограничные"
    malignant = "злокачественные", "злокачественные"


class MyomatousNodeCount(models.TextChoices):
    one = "один(м.б.доминирующий)", "один(м.б.доминирующий)"
    two_three = "2 - 3", "2 - 3"
    four_five = "4 - 5", "4 - 5"
    over_five = "более 5", "более 5"


class ControlPoints(models.TextChoices):
    three = "3", "3 месяца"
    six = "6", "6 месяцев"
    eleven = "12", "12 месяцев"
    year = "24", "24 месяца"
    mounth36 = "36", "36 месяцев"


class BaseAnketa(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True)
    full_name = models.CharField("ФИО", max_length=200)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.CharField(max_length=15, choices=Age.choices)
    height = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.full_name} - {self.age}"

    class Meta:
        verbose_name = "Базовая анкета"
        verbose_name_plural = "Базовые анкеты"

    def populate_percent(self):
        periods = PeriodsAnketa.objects.filter(base_anketa=self)
        if not periods:
            return 25
        doctor = DoctorAnketa.objects.filter(base_anketa=self)
        if not doctor:
            return 50
        artery = ArteryEmbolizationModel.objects.filter(base_anketa=self)
        if not artery:
            return 75
        return 100


class PeriodsAnketa(models.Model):
    base_anketa = models.ForeignKey(BaseAnketa, on_delete=models.CASCADE, null=True)
    menarche = models.CharField(max_length=20, choices=Menarche.choices)
    periods_type = models.CharField(max_length=20, choices=PeriodsType.choices)
    year_break = models.IntegerField()
    periods_break_variant = models.CharField(max_length=20, choices=Menarche.choices)
    break_type = models.CharField(max_length=20, choices=PeriodsType.choices)
    blood = models.BooleanField()
    blood_year = models.IntegerField(null=True, blank=True)
    #
    # dt_created = models.DateTimeField(auto_now_add=True)
    pregnancy_parity = models.IntegerField(null=True, blank=True)
    childbirth_count = models.IntegerField(null=True, blank=True)
    abortion_count = models.IntegerField(null=True, blank=True)
    misbirth_count = models.IntegerField("Выкидышей", null=True, blank=True)
    infertility_treatment = models.BooleanField(null=True, blank=True)
    brt_program = models.BooleanField(null=True, blank=True)
    contraception = models.CharField(max_length=50, choices=Contraception.choices)
    diseases_of_the_mammary_glands = models.CharField(
        "Заболевания молочных желез",
        max_length=50,
        choices=MammaryDiseases.choices,
        null=True,
        blank=True,
    )
    somatic_status = models.BooleanField("Соматический статус", null=True, blank=True)
    thyroid_gland_Pathology = models.BooleanField(
        "Патология щитовидной железы", null=True, blank=True
    )
    anemia = models.BooleanField("Анемия", null=True, blank=True)
    diagnosis_year = models.IntegerField(
        "Год постановки диагноза", null=True, blank=True
    )
    complaints_1 = models.BooleanField(
        "боль в пояснице, боли внизу живота, снижающие качество жизни"
    )
    complaints_2 = models.BooleanField(
        "симптомы сдавления смежных органов (прямая кишка, мочевой пузырь, мочеточники)"
    )
    complaints_3 = models.BooleanField("болезненные половые акты")
    complaints_4 = models.BooleanField("очень обильные кровотечения во время месячных")
    complaints_5 = models.BooleanField("«мазня» в середине цикла")
    complaints_6 = models.BooleanField("снижение показателя гемоглобина")
    hemoglobin = models.FloatField("Гемоглобин", null=True, blank=True)

    class Meta:
        verbose_name = "Менструальная функция"
        verbose_name_plural = "Менструальная функция"


class DoctorAnketa(models.Model):
    base_anketa = models.ForeignKey(BaseAnketa, on_delete=models.CASCADE, null=True)
    contraception = models.CharField(
        "Классификация миомы матки Международной федерации гинекологии и акушерства",
        max_length=100,
    )
    myomatous_node_count = models.CharField(
        "Количество миоматозных узлов",
        max_length=50,
        choices=MyomatousNodeCount.choices,
    )
    diagnosis_year = models.IntegerField(
        "Объем миоматозных узлов, см3", null=True, blank=True
    )
    with_adenomyosis = models.BooleanField(
        "Сочетание с аденомиозом", null=True, blank=True
    )
    resistance_index = models.CharField(
        "Индекс резистентности по данным ДМ", max_length=20, null=True, blank=True
    )
    mioma1 = models.BooleanField("прогестагены")
    mioma2 = models.BooleanField("комбинированные оральные контрацептивы")
    mioma3 = models.BooleanField("агонисты гонадотропинрилизинг-гормона (аГн-РГ)")
    mioma4 = models.BooleanField("мифепристон")
    mioma5 = models.BooleanField("улипристала ацетат")
    # "Хирургическое лечение миомы матки в анамнезе "
    # "surgical_treatment_in_history of uterine fibroids in history "
    surgical_treatment_in_history1 = models.BooleanField(
        "консервативная миомэктомия лапароскопическим доступом"
    )
    surgical_treatment_in_history1_year = models.IntegerField(
        "Год", null=True, blank=True
    )
    surgical_treatment_in_history2 = models.BooleanField(
        "консервативная миомэктомия лапаротомным доступом, год_____"
    )
    surgical_treatment_in_history2_year = models.IntegerField(
        "Год", null=True, blank=True
    )
    surgical_treatment_in_history3 = models.BooleanField(
        "гистероскопическое удаление подслизистых миоматозных узлов, год ______"
    )
    surgical_treatment_in_history3_year = models.IntegerField(
        "Год", null=True, blank=True
    )
    surgical_treatment_in_history4 = models.BooleanField(
        "окклюзия маточных артерий с помощью эмболизации, год_____"
    )
    surgical_treatment_in_history4_year = models.IntegerField(
        "Год", null=True, blank=True
    )
    # indication_for_treatment
    indication_for_treatment1 = models.BooleanField("АМК, приводящие к анемии")
    indication_for_treatment2 = models.BooleanField(
        "Хроническая тазовая боль, снижающая качество жизни"
    )
    indication_for_treatment3 = models.BooleanField(
        "Симптомы сдавления смежных органов (прямая кишка, мочевой пузырь, мочеточники)"
    )
    indication_for_treatment4 = models.BooleanField(
        "Большой размер опухоли (более 12 недель беременности)"
    )
    indication_for_treatment5 = models.BooleanField(
        "Быстрый рост опухоли (увеличение матки более чем на 4 недели беременности в течение 1 года)"
    )
    indication_for_treatment6 = models.BooleanField("Рост опухоли в постменопаузе")
    indication_for_treatment7 = models.BooleanField(
        "Подслизистое расположение узла миомы"
    )
    indication_for_treatment8 = models.BooleanField(
        "Межсвязочное и низкое (шеечное и перешеечное) расположение узлов миомы"
    )
    indication_for_treatment9 = models.BooleanField(
        "Нарушение репродуктивной функции (невынашивание беременности, бесплодие при отсутствии других причин"
    )
    indication_for_treatment10 = models.BooleanField(
        "Признаки нарушения кровообращения в узлах миомы матки (некроз, отек, гиалиноз)."
    )

    # Заполняет врач
    class Meta:
        verbose_name = "Анкета врача"
        verbose_name_plural = "Анкеты врачей"


class ArteryEmbolizationModel(models.Model):
    """Контрольные точки динамического наблюдения пациенток после проведенной ЭМА"""

    base_anketa = models.ForeignKey(BaseAnketa, on_delete=models.CASCADE, null=True)
    control_points = models.CharField(
        "Контрольные точки динамического наблюдения пациенток после проведенной ЭМА",
        max_length=20,
        choices=ControlPoints.choices,
        null=True,
        blank=True,
    )
    performance_criteria = models.CharField(
        "Критерии эффективности", max_length=256, null=True, blank=True
    )
    menstrual_function = models.CharField(
        "Менструальная функция", max_length=256, null=True, blank=True
    )
    menarche = models.CharField(
        "Цикличность менструальных выделений",
        max_length=20,
        choices=Menarche.choices,
        null=True,
        blank=True,
    )
    periods_type = models.CharField(
        "Тип", max_length=20, choices=PeriodsType.choices, null=True, blank=True
    )
    complaints_1 = models.BooleanField(
        "боль в пояснице, боли внизу живота, снижающие качество жизни"
    )
    complaints_2 = models.BooleanField(
        "симптомы сдавления смежных органов (прямая кишка, мочевой пузырь, мочеточники)"
    )
    complaints_3 = models.BooleanField("болезненные половые акты")
    complaints_4 = models.BooleanField("очень обильные кровотечения во время месячных")
    complaints_6 = models.BooleanField("показатель уровня гемоглобина ")
    hemoglobin = models.FloatField("Гемоглобин", null=True, blank=True)
    contraception = models.CharField(
        "Классификация миомы матки Международной федерации гинекологии и акушерства",
        max_length=100,
        null=True,
        blank=True,
    )
    myomatous_node_count = models.CharField(
        "Количество миоматозных узлов",
        max_length=50,
        choices=MyomatousNodeCount.choices,
        null=True,
        blank=True,
    )
    diagnosis_year = models.IntegerField(
        "Объем миоматозных узлов, см3", null=True, blank=True
    )
    with_adenomyosis = models.BooleanField(
        "Сочетание с аденомиозом", null=True, blank=True
    )

    class Meta:
        verbose_name = "Cелективная эмболизация маточных артерий"
        verbose_name_plural = "Cелективные эмболизации маточных артерий"
