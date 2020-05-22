# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   
    # path('admin/', admin.site.urls),
    path('', views.home_page, name='homepage'),
    path('newuser/', views.newuser_view, name='newuser'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')


]