from django.contrib import admin
from django.urls import path
from telesystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('find/', views.find, name="find"),
    path('add/', views.add, name="add"),
    path('add_number/<int:pk>', views.add_number, name="add_number")
]
