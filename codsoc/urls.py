from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('secure-admin-url/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('modules.urls'))
]
