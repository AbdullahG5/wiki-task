from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry , name="entry"),
    path('search/', views.search, name='search'),
    path("random_page/" ,views.random, name='R_P'),
    path("Create_New_Page/" ,views.Create_New_Page, name='CNP'),
    path("edit/",views.edit,name="edit"),
    path("save/",views.save_the_edit,name="save"),


]
