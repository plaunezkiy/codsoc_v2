from django.shortcuts import render
from .models import Module


def index(request):
    modules = Module.objects.all()
    return render(request, "index.html", {"modules": modules})
