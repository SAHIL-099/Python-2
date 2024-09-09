from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
    path('blog_list', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:pk>/delete/',views.delete_blog, name='delete_blog'),
    path('create/', views.create_blog, name='create_blog'),
]
