from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.login, name='login'),
    path('home/', admin.site.urls), #homeView
]
