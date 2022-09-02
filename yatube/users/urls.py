from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView
from django.urls import path

from .views import LoginUser, SignUp

app_name = 'users'

urlpatterns = [
    path('logout/',
         LogoutView.as_view(template_name='users/logged_out.html'),
         name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/',
         LoginUser.as_view(template_name='users/login.html'),
         name='login'
         ),
    path('password_change/',
         PasswordChangeView.as_view(template_name='users/password_change_form.html'),
         name='password_change_form'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html')),
    path('password_reset/',PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset_form' )
]
