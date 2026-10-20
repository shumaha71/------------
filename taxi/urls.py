from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "login/",
        LoginView.as_view(template_name="taxi/login.html"),
        name="login",
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),

    path(
        "passenger/",
        views.passenger_dashboard, name='passenger_dashboard'
    ),

    path(
        "dashboard/",
        views.dashboard, name="dashboard"
    ),

    path(
        "driver/",
        views.driver_dashboard, name="driver_dashboard"
    ),

    path(
        "management/",
        views.admin_dashboard,
        name="admin_dashboard",
    )
]