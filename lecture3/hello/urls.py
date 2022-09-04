from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edilson", views.edilson, name="edilson"),
path("david", views.david, name="david")
]
