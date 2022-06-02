from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('studentclick', views.studentclick_view),
    path('',views.home,name='studenthome'),
    path('register',views.register,name='studentregister'),
    # path('login',views.login,name='login'),
    path('handeLogin', views.handeLogin, name="handeLogin"),
    path('logout', views.handelLogout, name="handleLogout"),

    # path('logout', views.handelLogout, name="handleLogout"),
]
