from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.telesystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('find/', views.find, name="find"),
    path('add/', views.add, name="add"),
    path('add_number/<int:pk>', views.add_number, name="add_number"),
    path('subscriber/<int:pk>', views.sub_change, name="sub_change"),
    path('subscriber_delete/<int:pk>', views.sub_delete, name="sub_delete")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
