"""
URL configuration for dcloak project.

1. admin
2. keycloak login
3. primary app
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # redirect login immediately to keycloak
    path("accounts/login/", RedirectView.as_view(url="/accounts/oidc/keycloak/login/?process=login", permanent=False)),
    path('accounts/', include('allauth.urls')),
    path('', include("primary.urls"))
]
