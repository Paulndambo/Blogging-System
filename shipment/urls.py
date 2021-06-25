from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path("search/", views.search, name="search"),
    path("shipment-tracking/", views.tracking,name="shipment-tracking"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
]