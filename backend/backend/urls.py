from django.contrib import admin
from django.urls import path, include
from api.views.game import CreateUserView, GetUserView, DocumentationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", DocumentationView.as_view(), name="docs_root"),
    path("<str:filename>", DocumentationView.as_view(), name="docs"),
    path("admin/", admin.site.urls),
    path("api/user/", GetUserView.as_view(), name="get_user"),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]
