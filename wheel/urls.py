from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_wheel, name='create_wheel'),
    path('wheel/<int:wheel_id>/', views.wheel_detail, name='wheel_detail'),
    path('wheel/<int:wheel_id>/add-item/', views.add_wheel_item, name='add_wheel_item'),
    path('data/', views.show_data, name='show_data'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='wheel/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] 