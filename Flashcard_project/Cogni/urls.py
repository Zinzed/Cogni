from django.contrib import admin
from django.urls import path

from django.urls import path, include
#from .views import main
from .views import CardListView, CardCreateView, CardUpdateView, CardDeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [

    path("", CardListView.as_view(), name="CardList"),
    path("new", CardCreateView.as_view(), name="CardCreate"),
    path("edit/<int:pk>",CardUpdateView.as_view(),name="CardUpdate"),
    path("delete/<int:pk>", CardDeleteView.as_view(), name="CardDelete"),
]

urlpatterns += staticfiles_urlpatterns()
