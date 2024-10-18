from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',views.login_page, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home,  name='home'),
    path('dashboard/', views.dash, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('list_items/', views.list_items, name="admin_list"),
    path('shop/', views.shop, name='shop')
]