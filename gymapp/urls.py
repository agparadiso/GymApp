from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from gyms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('signup/admin/', views.AdminSignUp.as_view(), name='adminsignup'),
    path('admin_home/', views.AdminHome),
]
