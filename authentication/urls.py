from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views as app_level_views
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='auth/login.html'),name='login'),
     path('logout/', app_level_views.logout_user, name="logout"),
    path('register/',app_level_views.register,name='register')
]
