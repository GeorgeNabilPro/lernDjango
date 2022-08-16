from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("george", views.greet1, name="greet_george"),
    path("<str:name>", views.greet2, name="greeting_someone"),
]
