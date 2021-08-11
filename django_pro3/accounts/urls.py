from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path(
        "login/",
        LoginView.as_view(template_name="accounts/login_form.html"),
        name="login",
    ),
    path("profile/", views.profile, name="profile"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]
