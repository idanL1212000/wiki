from tkinter.font import names

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.visitPage, name="entry"),
    path("random", views.randomPage, name="random"),
    path("add", views.addPage, name="add"),
    path("wiki/<str:title>/edit", views.editPage, name="edit"),
]
