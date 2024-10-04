from django.contrib import admin
from django.urls import path , include
from my_app import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

urlpatterns = [
    
    path("",views.index,name="index"),
    path("home",views.home,name="home"),
    path("sign_in",views.sign_in,name="sign_in"),
    # path("account_view",views.account_view,name="account_view"),
    path("course",views.course,name="course"),
    path('logout/', views.logout_view, name='logout'),
    path("about",views.about,name="about"),
    path("help",views.help,name="help"),
    path("course_xe",views.course_xe,name="course_xe"),
    

    path('login/', views.login_view, name='login'),

]
