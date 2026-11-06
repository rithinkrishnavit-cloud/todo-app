from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("home/", views.home, name="home"),
    path("add_todo/", views.add_todo, name="add_todo"),
    # <int:id> = Accepts an integer value from the URL.
    path("complete/<int:id>/", views.complete_todo, name="complete_todo"),
    path("delete/<int:id>/", views.delete_todo, name="delete_todo"),
    path("update/<int:id>/", views.update_todo, name="update_todo"),
]
