from django.urls import path
from . views import UserRegisterView, UserEditView, PasswordsChangeView, password_success
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    path("password/", PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    #path("password/", auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path("password_success/", password_success, name="password_success"),
]
