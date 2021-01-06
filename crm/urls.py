from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from core import views
from django.contrib.auth.decorators import login_required #para validar o login no index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", login_required(TemplateView.as_view(template_name="index.html")), name="index"),
    path("login/", views.login, name="homepage"),
    path("logout/", views.logout, name="logout"),
    path("login/submit", views.submit_login, name="submit_login"),
    path("customer/", include("customer.urls"))
]
