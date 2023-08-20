# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import logging

from django import template
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views import View

from .forms import AnketaForm, ArteryEmbolizationForm, DoctorForm, PeriodsForm
from .models import BaseAnketa, PeriodsAnketa, DoctorAnketa, ArteryEmbolizationModel


logger = logging.getLogger(__name__)


class NewAnketaView(View):
    template_name = "home/anketa_base.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            context={
                "form": AnketaForm(None),
            },
        )

    def post(self, request):
        form = AnketaForm(request.POST, request.FILES)

        if form.is_valid():
            if request.user.is_authenticated:
                user = request.user
            else:
                user = User.objects.create_user(
                    username="anonymous",
                    password=User.objects.make_random_password(),
                )
                user.username = f"anonymous_{user.id}"
                user.save(update_fields=["username"])
                # login
                auth.login(request, user)

            anketa = form.save(commit=False)
            anketa.owner = user
            anketa.save()
            return HttpResponseRedirect(
                reverse("periods", kwargs={"pk": form.instance.id}),
            )

        context = {
            "form": form,
        }
        return render(request, self.template_name, context=context)


class AnketaView(View):
    template_name = "home/anketa_base.html"
    form_class = AnketaForm
    next_url = "periods"

    _anketa = None

    def get_base_anketa(self, pk):
        if self._anketa:
            return self._anketa
        try:
            self._anketa = BaseAnketa.objects.get(pk=pk)
        except BaseAnketa.DoesNotExist:
            raise Http404

        return self._anketa

    def get_current_anketa(self, pk):
        return self.get_base_anketa(pk)

    def get_form(self, *args, **kwargs):
        return self.form_class(*args, **kwargs)

    def check_access(self, request, pk):
        if not request.user.is_authenticated:
            return False

        anketa = self.get_base_anketa(pk)
        print(anketa.owner, request.user)
        if anketa.owner == request.user:
            return True

        return False

    def save_anketa(self, anketa, pk):
        anketa.save()

    def get(self, request, pk):
        if not self.check_access(request, pk):
            logger.warning(f"User {request.user} tried to access anketa {pk}")
            return HttpResponseRedirect(reverse("home"))

        # get anketa
        form = self.get_form(instance=self.get_current_anketa(pk))
        context = {
            "form": form,
            "base_anketa": self.get_base_anketa(pk),
        }
        return render(request, self.template_name, context=context)

    def post(self, request, pk):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))

        form = self.get_form(
            request.POST, request.FILES, instance=self.get_current_anketa(pk)
        )

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(
                reverse(self.next_url, kwargs={"pk": self.get_base_anketa(pk).id}),
            )

        context = {"form": form}
        return render(request, self.template_name, context=context)


class PeriodsView(AnketaView):
    template_name = "home/anketa_periods.html"
    form_class = PeriodsForm
    next_url = "doctor"

    def get_current_anketa(self, pk):
        base_anketa = self.get_base_anketa(pk)
        return PeriodsAnketa.objects.filter(base_anketa=base_anketa).first()

    def save_anketa(self, anketa, pk):
        anketa.base_anketa = self.get_base_anketa(pk)
        anketa.save()


class DoctorView(AnketaView):
    template_name = "home/anketa_doctor.html"
    form_class = DoctorForm
    next_url = "artery_embolization"

    def get_current_anketa(self, pk):
        base_anketa = self.get_base_anketa(pk)
        return DoctorAnketa.objects.filter(base_anketa=base_anketa).first()

    def save_anketa(self, anketa, pk):
        anketa.base_anketa = self.get_base_anketa(pk)
        anketa.save()


class ArteryEmbolizationView(AnketaView):
    template_name = "home/anketa_artery_embolization.html"
    form_class = ArteryEmbolizationForm
    next_url = "anketa_success"

    def get_current_anketa(self, pk):
        base_anketa = self.get_base_anketa(pk)
        return ArteryEmbolizationModel.objects.filter(base_anketa=base_anketa).first()

    def save_anketa(self, anketa, pk):
        anketa.base_anketa = self.get_base_anketa(pk)
        anketa.save()


class AnketaSuccessView(View):
    def get(self, request, pk):
        return render(
            request,
            "home/anketa_success.html",
            context={
                "anketa": BaseAnketa.objects.get(pk=pk),
            },
        )


# @login_required(login_url="/login/")
def index(request):
    forms = {
        "form": AnketaForm(None),
        "periods_form": PeriodsForm(None),
        "doctor_form": DoctorForm(None),
        "artery_embolization_form": ArteryEmbolizationForm(None),
    }

    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "form":
            forms[form_type] = AnketaForm(request.POST, request.FILES)
        if form_type == "periods_form":
            forms[form_type] = PeriodsForm(request.POST)
        if form_type == "doctor_form":
            forms[form_type] = DoctorForm(request.POST)
        if form_type == "artery_embolization_form":
            forms[form_type] = ArteryEmbolizationForm(request.POST)

    html_template = loader.get_template("home/anketa.html")
    context = {"segment": "index", **forms}

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "form" and forms[form_type].is_valid():
            forms[form_type].save(commit=True)
            return HttpResponse("Форма сохранена")

        if form_type == "periods_form" and forms[form_type].is_valid():
            forms[form_type].save(commit=True)
            return HttpResponse("Форма Менструальная функция сохранена")

        if form_type == "doctor_form" and forms[form_type].is_valid():
            forms[form_type].save(commit=True)
            return HttpResponse("Форма врача сохранена")

        if form_type == "artery_embolization_form" and forms[form_type].is_valid():
            forms[form_type].save(commit=True)
            return HttpResponse(
                "Техника выполнения селективной эмболизации маточных артерий"
            )

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split("/")[-1]

        if load_template == "admin":
            return HttpResponseRedirect(reverse("admin:index"))
        context["segment"] = load_template

        html_template = loader.get_template("home/" + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template("home/page-404.html")
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template("home/page-500.html")
        return HttpResponse(html_template.render(context, request))
