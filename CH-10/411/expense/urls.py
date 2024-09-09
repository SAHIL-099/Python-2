from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('report/', views.expense_report, name='expense_report'),
]   
