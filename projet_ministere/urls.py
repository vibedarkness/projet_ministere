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
    path('index_staff', views.index_staff,name="index_staff"),
    path('client', views.nouveau_client,name="client"),
    path('client/add_facture/<int:client_id>', views.ajouter_facture,name="ajouter_facture"),
    path('client/add_ba/<int:client_id>', views.ajouter_ba,name="ajouter_ba"),
    path('add_staff', views.add_staff,name="add_staff"),
    path('do_staff', views.do_staff,name="do_staff"),
    path('voir/attestation/<int:client_id>', views.voir,name="voir_admin"),
    path('voir_staff/facture/<int:client_id>', views.voir_staff,name="voir_staff"),
    path('voir_ba/bordereau/<int:client_id>', views.voir_ba,name="voir_ba"),
    path('logout_user', views.logout_user,name="logout_user"),
    path('do_client', views.do_client, name="do_client"),
        # path('do_facture', views.do_facture, name="do_facture"),
    path('voir_facture/facture/<int:client_id>/<int:facture_id>', views.voir_facture, name="voir_facture"),
    path('voir_ba/bordereau/<int:client_id>/<int:ba_id>', views.ba, name="ba"),
    path('voir_attestation/attestation/<int:client_id>/<int:facture_id>', views.voir_attestation, name="voir_attestation"),
    path("client/delete_client/<int:client_id>", views.delete_client, name='delete_client'),
    # path("client/update_client/<int:client_id>", views.modifier_client, name='modifier_client'),
    # path("client/update_client/<int:client_id>", views.up_client, name='modifier_client'),
    # path("client/ajout_facture/<int:client_id>", views.nouveau_facture, name='ajout_facture'),
]
