
from django.contrib import admin
from django.urls import path

from async_app.views import http_call_async


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "async/",
        http_call_async,
        name="http_call_async"
    ),
]
