from django.conf.urls import handler404, handler500 # noqa
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# handler404 = "modules.views.page_not_found" # noqa
# handler500 = "modules.views.server_error" # noqa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('modules.urls'))
]
