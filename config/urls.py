from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from faq.views import home

def redirect_to_api(request):
    return HttpResponseRedirect("/api/faqs/")

urlpatterns = [
    path("", home, name="home"),  # New homepage view
    path("admin/", admin.site.urls),
    path("api/", include("faq.urls")),
]
