from django.urls import path, include

from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register("api/modules", views.ModuleView)

urlpatterns = [
    path("", views.index, name="index"),
    path("module/", views.modules_app)
]

urlpatterns += router.urls
