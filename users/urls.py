from django.urls import path
from . import views as userViews
from django.contrib.auth import views as authViews


urlpatterns = [
    path('reg/', userViews.register, name='reg'),
    path('', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('profile/', userViews.profile, name='profile'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit')
]


