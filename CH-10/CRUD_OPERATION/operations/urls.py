from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.login_user,name="login"),
    path("signup/",views.signup,name="signup"),
    path("student/",views.student,name="student"),
    path("logout/",views.logout_user,name="logout"),
    path("update/<int:id>/",views.update,name='update'),
    path("delete/<int:id>/",views.delete,name='delete'),
    path("search/",views.search,name="search"),
]
