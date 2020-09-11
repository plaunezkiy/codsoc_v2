from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from modules.models import Module
from modules.serializers import ModuleSerializer


def index(request):
    return render(request, "index.html")


def modules_app(request):
    return render(request, "main_app.html")


class ModuleView(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
