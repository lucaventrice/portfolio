from django.conf.urls import include, url
from django.urls import path
from users import views


urlpatterns = [
    path("", views.dashboard, name="users_dashboard"),
    path("register/", views.register, name="register"),
] 