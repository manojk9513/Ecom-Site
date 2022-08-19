from user import views as user_view
from django.contrib.auth import views as auth_view
from django.urls import path
from shop import views as shop_views


urlpatterns = [
    path('',shop_views.index,name='index'),
    path('register/',user_view.register,name="register"),
    path('login/',auth_view.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
]