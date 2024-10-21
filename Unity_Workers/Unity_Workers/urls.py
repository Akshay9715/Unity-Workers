"""
URL configuration for Unity_Workers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.language_popup,name='language_popup'),
    path('client_form/',views.client_form,name='client_form'),
    path('client_mobile_verification',views.client_mobile_verification,name='client_mobile_verification'),
    path('client_otp_verification',views.client_otp_verification,name='client_otp>verification.html'),
    path('client_payment',views.client_payment,name='client_payment'),
    path('home_page',views.home_page,name='home_page'),
    path('worker_login_page',views.worker_login_page,name='worker_login_page'),
    path('worker_registration_form',views.worker_registration_form,name='worker_registration_form')
]
