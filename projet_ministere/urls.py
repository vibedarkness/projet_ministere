"""projet_ministere URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Main import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.login,name="login"),
    path('do_login', views.do_login, name="do_login"),
    path('index', views.index,name="index"),
    path('client', views.nouveau_client,name="client"),
    path('add_facture', views.nouveau_facture,name="add_facture"),
    path('voir', views.voir,name="voir"),
    path('logout_user', views.logout_user,name="logout_user"),
    path('do_client', views.do_client, name="do_client"),
]
