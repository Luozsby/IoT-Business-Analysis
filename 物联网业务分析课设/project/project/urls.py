"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mqttapp import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('index/',views.index),
    path('user/list/',views.user_list),
    path('user/add/',views.user_add),

    path('login/',views.login),


    # path('orm/',views.orm),

    #用户列表
    path('info/list',views.info_list),
    #添加用户
    path('info/add',views.info_add),
    #删除用户
    path('info/delete',views.info_delete),
    


    #数据
    path('sensor_data/', views.sensor_data),
    path('mqtt_publish/', views.mqtt_publish, name='mqtt_publish'),

]
