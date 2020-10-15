from django.contrib import admin
from django.urls import include, path
from users.views import register

urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path("blog/", include("blog.urls")),
    path("users/", include("users.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
    path("oauth/", include("social_django.urls")),
]
