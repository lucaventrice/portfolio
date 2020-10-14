from django.conf.urls import include, url
from django.urls import path
from users import views


urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    path("", views.dashboard, name="users_dashboard"),
] 