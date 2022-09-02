from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("avi/", views.avi),
    path("phone/", views.phone),
    path("login/", views.user),
    path("signup/", views.signup),
    path("signout/", views.signout),

]