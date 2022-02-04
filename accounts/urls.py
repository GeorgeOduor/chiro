# from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path("signin",views.LoginPage.as_view(),name='signin'),
    path("signup",views.SignUp.as_view(),name='signup'),
    path("password_reset",views.ResetPasswordView.as_view(),name='password_reset'),
    path("logout",views.logout_view,name='logout'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile',views.ProfileView,name='profile'),

]
