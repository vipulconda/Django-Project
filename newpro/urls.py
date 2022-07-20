from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path("save_contact", views.contact, name="contact"),
]