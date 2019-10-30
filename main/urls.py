from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.Home, name="home"),
    path("history/", views.History, name="history"),
    path("<pk>/", views.ListArticles, name="list"),
    
]