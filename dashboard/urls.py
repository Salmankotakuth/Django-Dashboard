from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('tables', views.tables, name='tables'),
    path('billing', views.billing, name='billing'),
    path('virtual_reality', views.virtual_reality, name='virtual_reality'),
    path('rtl', views.rtl, name='rtl'),
    path('notifications', views.notifications, name='notifications'),
    path('profile', views.profile, name='profile'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up, name='sign_up'),
]