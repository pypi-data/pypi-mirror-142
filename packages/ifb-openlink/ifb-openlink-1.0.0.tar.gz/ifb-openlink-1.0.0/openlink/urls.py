"""openlink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar

# from openlink.core.admin import admin_site
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "OPENLINK Database administration"
admin.site.site_title = "OPENLINK administration"
admin.site.index_title = "OPENLINK Site Administration"

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    path("", include("openlink.core.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("django-rq/", include("django_rq.urls")),
    path('oidc/', include('mozilla_django_oidc.urls')),
]
