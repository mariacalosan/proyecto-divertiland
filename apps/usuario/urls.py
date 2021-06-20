from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from .views import RegistroUsuario, logout_view

app_name = 'usuario'

urlpatterns = [
    path('',
        LoginView.as_view(template_name='usuario/index.html'),
        name='login'
        ),
    path('registrar/',
         RegistroUsuario.as_view(),
         name="registrar"),
    path('logout/',
         logout_view,
         name='logout'),
    path('reset/password_reset',
         PasswordResetView.as_view(), {
             'template_name': 'usuario/password/password_reset_form.html',
             'email_template_name': 'usuario/password/password_reset_email.html'
         },
         name='password_reset'),
    path('password_reset_done',
         PasswordResetDoneView.as_view(), {
             'template_name': 'usuario/password/password_reset_done.html'
         },
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), {
             'template_name': 'usuario/password/password_reset_confirm.html'
         },
         name='password_reset_confirm'
         ),
    path('reset/done',
         PasswordResetCompleteView.as_view(), {
             'template_name': 'usuario/password/password_reset_complete.html'
         },
         name='password_reset_complete'),
]
