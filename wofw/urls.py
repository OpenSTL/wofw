__author__ = 'jesselevine'

from django.conf.urls import url

from . import views

urlpatterns = [

    # ex: /
    url(r'^$', views.index, name="index"),

    # ex: /wards/
    url(r'^wards/$', views.wards, name="wards"),

    # ex: /wards/14/
    url(r'^wards/(?P<wardnumber>[0-9]+)$', views.ward_detail, name="ward_detail"),

    # ex: /aldermen/
    url(r'^aldermen/$', views.aldermen, name="aldermen"),

    # ex: /aldermen/smith/
    url(r"^aldermen/(?P<alderman_name>[a-z ,.'-]+)$", views.alderman_detail, name="alderman_detail"),

    # ex: /bills/
    url(r'^bills/$', views.bills, name="bills"),

    # ex: /bills/208/
    url(r'^bills/(?P<billnumber>[0-9]+)$', views.bill_detail, name="bill_detail")

]
