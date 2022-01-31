# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .forms import AnketaForm, PeriodsForm


# @login_required(login_url="/login/")
def index(request):
    forms = {
        "form": AnketaForm(None),
        "periods_form": PeriodsForm(None),
    }

    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "form":
            forms[form_type] = AnketaForm(request.POST, request.FILES)
        if form_type == "periods_form":
            forms[form_type] = PeriodsForm(request.POST)

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
