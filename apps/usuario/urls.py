from django.contrib.auth import login
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, logout_then_login
from django.urls import path
from apps.usuario.views import RegistroUsuario

app_name = 'usuario'

urlpatterns = [
  	path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('accounts/login/', login, {'template_name':'index.html'}, name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('reset/password_reset', PasswordResetView.as_view(),
        {'template_name':'registration/password_reset_form.html',
        'email_template_name': 'registration/password_reset_email.html'},
        name='password_reset'),
    path('password_reset_done', PasswordResetDoneView.as_view(),
        {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_done'),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(),
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    path('reset/done', PasswordResetCompleteView.as_view(), {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
]