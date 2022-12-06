from django.urls import path

from . import views

urlpatterns = [

    path(r"<int:month>/", views.mounthly_challenge_by_number),
    path(r"<str:month>/", views.mounthly_challenge)
]
